# Phụ lục

## Phụ lục A: Mã nguồn Python cho việc xử lý dữ liệu SLAM

```python
# Mã nguồn cho việc xử lý dữ liệu SLAM
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_slam_data(file_path):
    """
    Tải dữ liệu SLAM từ file gzip

    Parameters:
    -----------
    file_path : str
        Đường dẫn đến file dữ liệu SLAM

    Returns:
    --------
    DataFrame
        Dữ liệu SLAM đã được tải
    """
    return pd.read_csv(file_path, compression='gzip')

def preprocess_slam_data(df):
    """
    Tiền xử lý dữ liệu SLAM

    Parameters:
    -----------
    df : DataFrame
        DataFrame chứa dữ liệu SLAM

    Returns:
    --------
    DataFrame
        Dữ liệu SLAM đã được tiền xử lý
    """
    # Loại bỏ các dòng có giá trị thiếu
    df = df.dropna()

    # Chuyển đổi thời gian từ giây sang ngày
    df['time_since_last_attempt_days'] = df['time_since_last_attempt'] / (24 * 60 * 60)

    # Tính tỷ lệ đúng
    df['correct_ratio'] = df['num_correct'] / df['num_attempts']

    # Tính tần suất lặp lại (số lần thử trung bình mỗi ngày)
    # Giả sử thời gian học tập là 30 ngày
    df['repetition_frequency'] = df['num_attempts'] / 30

    return df

def split_data(df, test_size=0.2, random_state=42):
    """
    Chia dữ liệu thành tập huấn luyện và tập kiểm tra

    Parameters:
    -----------
    df : DataFrame
        DataFrame chứa dữ liệu SLAM đã được tiền xử lý
    test_size : float, default=0.2
        Tỷ lệ dữ liệu dành cho tập kiểm tra
    random_state : int, default=42
        Seed cho việc tạo số ngẫu nhiên

    Returns:
    --------
    tuple
        (X_train, X_test, y_train, y_test)
    """
    # Chọn các đặc trưng
    features = ['num_attempts', 'num_correct', 'time_since_last_attempt_days',
                'correct_ratio', 'repetition_frequency']

    X = df[features]
    y = df['label']  # 0: đúng, 1: sai

    return train_test_split(X, y, test_size=test_size, random_state=random_state)
```

## Phụ lục B: Mã nguồn Python cho việc xây dựng và đánh giá mô hình

```python
# Mã nguồn cho việc xây dựng và đánh giá mô hình
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def train_logistic_regression(X_train, y_train):
    """
    Huấn luyện mô hình Logistic Regression

    Parameters:
    -----------
    X_train : DataFrame
        Đặc trưng của tập huấn luyện
    y_train : Series
        Nhãn của tập huấn luyện

    Returns:
    --------
    LogisticRegression
        Mô hình Logistic Regression đã được huấn luyện
    """
    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Huấn luyện mô hình
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train)

    return model, scaler

def train_random_forest(X_train, y_train):
    """
    Huấn luyện mô hình Random Forest

    Parameters:
    -----------
    X_train : DataFrame
        Đặc trưng của tập huấn luyện
    y_train : Series
        Nhãn của tập huấn luyện

    Returns:
    --------
    RandomForestClassifier
        Mô hình Random Forest đã được huấn luyện
    """
    # Huấn luyện mô hình
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    return model

def evaluate_model(model, X_test, y_test, scaler=None):
    """
    Đánh giá hiệu suất của mô hình

    Parameters:
    -----------
    model : object
        Mô hình đã được huấn luyện
    X_test : DataFrame
        Đặc trưng của tập kiểm tra
    y_test : Series
        Nhãn của tập kiểm tra
    scaler : StandardScaler, default=None
        Bộ chuẩn hóa dữ liệu (chỉ cần cho Logistic Regression)

    Returns:
    --------
    dict
        Các chỉ số đánh giá hiệu suất
    """
    # Chuẩn hóa dữ liệu nếu cần
    if scaler is not None:
        X_test_scaled = scaler.transform(X_test)
        y_pred = model.predict(X_test_scaled)
    else:
        y_pred = model.predict(X_test)

    # Tính toán các chỉ số đánh giá
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'confusion_matrix': conf_matrix
    }

def plot_feature_importance(model, feature_names):
    """
    Vẽ biểu đồ tầm quan trọng của các đặc trưng

    Parameters:
    -----------
    model : RandomForestClassifier
        Mô hình Random Forest đã được huấn luyện
    feature_names : list
        Tên của các đặc trưng
    """
    # Lấy tầm quan trọng của các đặc trưng
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    # Vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    plt.title('Tầm quan trọng của các đặc trưng')
    plt.bar(range(len(importances)), importances[indices], align='center')
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.tight_layout()
    plt.show()
```

## Phụ lục C: Mẫu dữ liệu SLAM

Dưới đây là một mẫu dữ liệu từ bộ dữ liệu SLAM của Duolingo:

| user_id | token | num_attempts | num_correct | time_since_last_attempt | label |
| ------- | ----- | ------------ | ----------- | ----------------------- | ----- |
| 123     | hello | 5            | 4           | 86400                   | 0     |
| 123     | world | 3            | 1           | 172800                  | 1     |
| 456     | hello | 2            | 2           | 43200                   | 0     |
| 456     | world | 1            | 0           | 0                       | 1     |
| 789     | hello | 7            | 6           | 259200                  | 0     |

_Chú thích_:

-   label = 0: Học viên trả lời đúng
-   label = 1: Học viên trả lời sai
-   time_since_last_attempt: Thời gian kể từ lần thử cuối (tính bằng giây)
