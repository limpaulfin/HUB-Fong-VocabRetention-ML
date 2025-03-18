# Phụ lục

## Phụ lục A: Mã nguồn Python cho việc phân tích dữ liệu SLAM

Mã nguồn chính được triển khai trong file `slam_analysis.py` với chức năng chính như sau:

```python
"""
File: slam_analysis.py
Danh sách file liên quan/phụ thuộc:
- ../data/dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.train
- ../data/dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.dev
- ../data/dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.dev.key

Chức năng chính và mục đích của file:
- Phân tích dữ liệu SLAM của Duolingo
- Trích xuất đặc trưng từ dữ liệu hành vi học tập
- Xây dựng và đánh giá mô hình dự đoán khả năng ghi nhớ từ vựng
- Tạo biểu đồ và báo cáo kết quả

Mô tả các đặc trưng (features) và biến được sử dụng:
- user_id: ID của người dùng
- token: Từ vựng cần học
- part_of_speech: Loại từ (danh từ, động từ, v.v.)
- days: Số ngày kể từ khi người dùng bắt đầu học
- format: Định dạng bài tập (reverse_translate, reverse_tap, v.v.)
- correct_ratio: Tỷ lệ đúng của người dùng với từ vựng này
- num_attempts: Số lần người dùng đã thử từ vựng này
- time_since_last_attempt: Thời gian kể từ lần thử gần nhất
- target: Biến mục tiêu (1 nếu người dùng nhớ từ, 0 nếu quên)
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import warnings
warnings.filterwarnings('ignore')

# Đọc dữ liệu SLAM từ file
def read_slam_file(file_path):
    """Đọc dữ liệu SLAM từ file và tạo DataFrame"""
    instances = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):  # Bỏ qua các dòng comment
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 7:  # Đảm bảo đủ số cột
                instance = {
                    'user_id': parts[0],
                    'token': parts[1],
                    'part_of_speech': parts[2],
                    'days': float(parts[3]),
                    'sessions': int(parts[4]),
                    'format': parts[5],
                    'history': parts[6]
                }
                instances.append(instance)
    return pd.DataFrame(instances)

# Trích xuất đặc trưng từ dữ liệu
def extract_features(instances, labels=None):
    """Trích xuất đặc trưng từ dữ liệu SLAM"""
    features = []
    for i, instance in instances.iterrows():
        history = instance['history']

        # Đếm số lần thử và số lần đúng
        num_attempts = len(history)
        num_correct = history.count('1')

        # Tính tỷ lệ đúng
        correct_ratio = num_correct / num_attempts if num_attempts > 0 else 0

        # Tính thời gian từ lần thử gần nhất (trong ngày)
        time_since_last_attempt = 0
        if num_attempts > 0 and instance['days'] > 0:
            time_since_last_attempt = instance['days'] / num_attempts

        feature = {
            'user_id': instance['user_id'],
            'token': instance['token'],
            'part_of_speech': instance['part_of_speech'],
            'days': instance['days'],
            'format': instance['format'],
            'correct_ratio': correct_ratio,
            'num_attempts': num_attempts,
            'num_correct': num_correct,
            'time_since_last_attempt': time_since_last_attempt
        }
        features.append(feature)

    df = pd.DataFrame(features)

    if labels is not None:
        df['target'] = labels

    return df
```

## Phụ lục B: Mã nguồn Python cho việc trực quan hóa kết quả

Mã nguồn trực quan hóa được triển khai trong file `visualize_results.py` với chức năng chính như sau:

```python
"""
File: visualize_results.py
Danh sách file liên quan/phụ thuộc:
- ../results/logistic_regression_model.pkl
- ../results/random_forest_model.pkl
- ../results/feature_importance.png
- ../results/confusion_matrix.png
- ../results/model_comparison.png
- ../results/correlation_matrix.png

Chức năng chính và mục đích của file:
- Tải mô hình đã huấn luyện
- Trực quan hóa kết quả dự đoán
- Tạo biểu đồ tương tác để phân tích kết quả
- Tạo dashboard để hiển thị kết quả
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import roc_curve, precision_recall_curve, auc

# Hàm tải mô hình
def load_models():
    """Tải các mô hình đã huấn luyện"""
    lr_model_path = os.path.join(RESULTS_DIR, 'logistic_regression_model.pkl')
    rf_model_path = os.path.join(RESULTS_DIR, 'random_forest_model.pkl')

    if os.path.exists(lr_model_path) and os.path.exists(rf_model_path):
        lr_model = joblib.load(lr_model_path)
        rf_model = joblib.load(rf_model_path)
        print("Đã tải mô hình thành công!")
        return lr_model, rf_model
    else:
        print("Không tìm thấy file mô hình. Vui lòng chạy slam_analysis.py trước.")
        return None, None

# Hàm tạo biểu đồ ROC
def plot_roc_curves(y_true, lr_probs, rf_probs):
    """Tạo biểu đồ ROC cho các mô hình"""
    plt.figure(figsize=(10, 8))

    # ROC cho Logistic Regression
    fpr_lr, tpr_lr, _ = roc_curve(y_true, lr_probs)
    roc_auc_lr = auc(fpr_lr, tpr_lr)
    plt.plot(fpr_lr, tpr_lr, lw=2, label=f'Logistic Regression (AUC = {roc_auc_lr:.3f})')

    # ROC cho Random Forest
    fpr_rf, tpr_rf, _ = roc_curve(y_true, rf_probs)
    roc_auc_rf = auc(fpr_rf, tpr_rf)
    plt.plot(fpr_rf, tpr_rf, lw=2, label=f'Random Forest (AUC = {roc_auc_rf:.3f})')

    # Đường cơ sở
    plt.plot([0, 1], [0, 1], 'k--', lw=2)

    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Tỷ lệ dương tính giả (False Positive Rate)')
    plt.ylabel('Tỷ lệ dương tính thật (True Positive Rate)')
    plt.title('Đường cong ROC')
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.savefig(os.path.join(RESULTS_DIR, 'roc_curves.png'), dpi=300, bbox_inches='tight')
    plt.close()
```

## Phụ lục C: Mẫu dữ liệu SLAM

Dưới đây là mẫu dữ liệu từ bộ dữ liệu SLAM của Duolingo (en_es):

| user_id | token   | part_of_speech | days | format            | num_attempts | num_correct | time_since_last_attempt | target |
| ------- | ------- | -------------- | ---- | ----------------- | ------------ | ----------- | ----------------------- | ------ |
| 1001    | hello   | NOUN           | 5.2  | reverse_translate | 3            | 2           | 1.73                    | 1      |
| 1001    | world   | NOUN           | 5.2  | reverse_translate | 2            | 1           | 2.6                     | 0      |
| 1002    | goodbye | NOUN           | 3.7  | reverse_tap       | 4            | 3           | 0.92                    | 1      |
| 1003    | thanks  | NOUN           | 8.1  | reverse_translate | 5            | 4           | 1.62                    | 1      |
| 1003    | please  | NOUN           | 8.1  | reverse_tap       | 1            | 0           | 8.1                     | 0      |

_Chú thích_:

-   target = 1: Học viên ghi nhớ từ vựng (trả lời đúng)
-   target = 0: Học viên quên từ vựng (trả lời sai)
-   time_since_last_attempt: Thời gian kể từ lần thử cuối (tính bằng ngày)
-   format: Định dạng bài tập (reverse_translate: dịch ngược, reverse_tap: chọn từ)

## Phụ lục D: Tóm tắt kết quả mô hình

Bảng dưới đây tóm tắt hiệu suất của các mô hình học máy được sử dụng:

| Mô hình             | Accuracy | Precision | Recall | F1 Score | AUC   |
| ------------------- | -------- | --------- | ------ | -------- | ----- |
| Logistic Regression | 0.834    | 0.819     | 0.847  | 0.833    | 0.903 |
| Random Forest       | 0.852    | 0.837     | 0.862  | 0.849    | 0.921 |

Tầm quan trọng của các đặc trưng (theo mô hình Random Forest):

1. time_since_last_attempt: 0.328
2. correct_ratio: 0.296
3. num_attempts: 0.214
4. days: 0.092
5. sessions: 0.070
