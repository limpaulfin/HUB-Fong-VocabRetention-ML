"""
File: slam_analysis.py
Danh sách file liên quan/phụ thuộc:
- dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.train
- dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.dev
- dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.dev.key

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

# Đường dẫn đến các file dữ liệu
TRAIN_PATH = "dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.train"
DEV_PATH = "dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.dev"
DEV_KEY_PATH = "dataverse_files/data_en_es.tar/data_en_es/en_es.slam.20190204.dev.key"

# Hàm đọc dữ liệu SLAM
def read_slam_file(file_path):
    """Đọc file dữ liệu SLAM và trả về danh sách các instance"""
    instances = []
    current_instance = {}
    current_tokens = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Bỏ qua dòng trống
            if not line:
                continue

            # Dòng metadata bắt đầu bằng #
            if line.startswith('#'):
                # Nếu đã có instance trước đó, lưu lại
                if current_tokens and 'user' in current_instance:
                    current_instance['tokens'] = current_tokens
                    instances.append(current_instance)
                    current_tokens = []

                # Bắt đầu instance mới
                if 'user:' in line:
                    current_instance = {}
                    parts = line.split()

                    for part in parts:
                        if part.startswith('#'):
                            continue
                        if ':' in part:
                            key, value = part.split(':', 1)
                            current_instance[key] = value

                # Xử lý dòng prompt nếu có
                if 'prompt:' in line:
                    prompt = line.replace('# prompt:', '').strip()
                    current_instance['prompt'] = prompt

            # Dòng token
            else:
                parts = line.split()
                if len(parts) >= 5:
                    token_id = parts[0]
                    token = parts[1]
                    pos = parts[2]
                    morphological_features = parts[3]
                    dependency_label = parts[4]

                    token_info = {
                        'token_id': token_id,
                        'token': token,
                        'pos': pos,
                        'morphological_features': morphological_features,
                        'dependency_label': dependency_label
                    }

                    current_tokens.append(token_info)

    # Thêm instance cuối cùng
    if current_tokens and 'user' in current_instance:
        current_instance['tokens'] = current_tokens
        instances.append(current_instance)

    return instances

# Hàm đọc file key (nhãn)
def read_key_file(file_path):
    """Đọc file key chứa nhãn và trả về dict ánh xạ token_id -> label"""
    labels = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) >= 2:
                token_id = parts[0]
                label = int(parts[1])
                labels[token_id] = label

    return labels

# Hàm trích xuất đặc trưng
def extract_features(instances, labels=None):
    """Trích xuất đặc trưng từ các instance và tạo DataFrame"""
    # Theo dõi lịch sử học tập của người dùng
    user_token_history = defaultdict(lambda: defaultdict(list))

    # Lưu trữ các đặc trưng
    features = []

    # Sắp xếp instances theo thời gian (days)
    sorted_instances = sorted(instances, key=lambda x: float(x.get('days', 0)))

    for instance in sorted_instances:
        user_id = instance.get('user', '')
        days = float(instance.get('days', 0))
        format_type = instance.get('format', '')

        for token_info in instance.get('tokens', []):
            token_id = token_info.get('token_id', '')
            token = token_info.get('token', '').lower()
            pos = token_info.get('pos', '')

            # Lấy nhãn nếu có
            label = labels.get(token_id, None) if labels else None

            # Tính toán các đặc trưng dựa trên lịch sử
            token_history = user_token_history[user_id][token]
            num_attempts = len(token_history)

            # Tính tỷ lệ đúng
            correct_ratio = 0
            if num_attempts > 0 and labels:
                correct_ratio = sum(1 for h in token_history if labels.get(h['token_id'], 0) == 1) / num_attempts

            # Tính thời gian kể từ lần thử gần nhất
            time_since_last_attempt = 0
            if num_attempts > 0:
                time_since_last_attempt = days - token_history[-1]['days']

            # Tạo đặc trưng
            feature = {
                'user_id': user_id,
                'token_id': token_id,
                'token': token,
                'pos': pos,
                'days': days,
                'format': format_type,
                'num_attempts': num_attempts,
                'correct_ratio': correct_ratio,
                'time_since_last_attempt': time_since_last_attempt
            }

            if label is not None:
                feature['target'] = label

            features.append(feature)

            # Cập nhật lịch sử
            user_token_history[user_id][token].append({
                'token_id': token_id,
                'days': days,
                'label': label
            })

    return pd.DataFrame(features)

# Hàm huấn luyện và đánh giá mô hình
def train_and_evaluate_models(X_train, y_train, X_test, y_test):
    """Huấn luyện và đánh giá các mô hình học máy"""
    # Chuẩn bị pipeline với scaling
    lr_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(max_iter=1000, random_state=42))
    ])

    rf_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestClassifier(random_state=42))
    ])

    # Tham số tối ưu hóa
    lr_params = {
        'model__C': [0.01, 0.1, 1, 10, 100]
    }

    rf_params = {
        'model__n_estimators': [100, 200],
        'model__max_depth': [None, 10, 20],
        'model__min_samples_split': [2, 5, 10]
    }

    # Tối ưu hóa mô hình
    lr_grid = GridSearchCV(lr_pipeline, lr_params, cv=3, scoring='roc_auc')
    rf_grid = GridSearchCV(rf_pipeline, rf_params, cv=3, scoring='roc_auc')

    # Huấn luyện mô hình
    print("Đang huấn luyện Logistic Regression...")
    lr_grid.fit(X_train, y_train)

    print("Đang huấn luyện Random Forest...")
    rf_grid.fit(X_train, y_train)

    # Lấy mô hình tốt nhất
    best_lr = lr_grid.best_estimator_
    best_rf = rf_grid.best_estimator_

    # Dự đoán
    lr_pred = best_lr.predict(X_test)
    rf_pred = best_rf.predict(X_test)

    lr_prob = best_lr.predict_proba(X_test)[:, 1]
    rf_prob = best_rf.predict_proba(X_test)[:, 1]

    # Đánh giá
    results = {
        'Logistic Regression': {
            'accuracy': accuracy_score(y_test, lr_pred),
            'precision': precision_score(y_test, lr_pred),
            'recall': recall_score(y_test, lr_pred),
            'f1': f1_score(y_test, lr_pred),
            'roc_auc': roc_auc_score(y_test, lr_prob),
            'confusion_matrix': confusion_matrix(y_test, lr_pred),
            'model': best_lr,
            'predictions': lr_pred,
            'probabilities': lr_prob
        },
        'Random Forest': {
            'accuracy': accuracy_score(y_test, rf_pred),
            'precision': precision_score(y_test, rf_pred),
            'recall': recall_score(y_test, rf_pred),
            'f1': f1_score(y_test, rf_pred),
            'roc_auc': roc_auc_score(y_test, rf_prob),
            'confusion_matrix': confusion_matrix(y_test, rf_pred),
            'model': best_rf,
            'predictions': rf_pred,
            'probabilities': rf_prob
        }
    }

    return results

# Hàm phân tích tầm quan trọng của đặc trưng
def analyze_feature_importance(models, feature_names):
    """Phân tích và trực quan hóa tầm quan trọng của đặc trưng"""
    # Logistic Regression
    lr_model = models['Logistic Regression']['model'].named_steps['model']
    lr_coef = lr_model.coef_[0]
    lr_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': np.abs(lr_coef)
    })
    lr_importance = lr_importance.sort_values('Importance', ascending=False)

    # Random Forest
    rf_model = models['Random Forest']['model'].named_steps['model']
    rf_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': rf_model.feature_importances_
    })
    rf_importance = rf_importance.sort_values('Importance', ascending=False)

    # Tạo biểu đồ
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 1, 1)
    sns.barplot(x='Importance', y='Feature', data=lr_importance.head(10))
    plt.title('Top 10 đặc trưng quan trọng nhất - Logistic Regression')
    plt.tight_layout()

    plt.subplot(2, 1, 2)
    sns.barplot(x='Importance', y='Feature', data=rf_importance.head(10))
    plt.title('Top 10 đặc trưng quan trọng nhất - Random Forest')
    plt.tight_layout()

    plt.savefig('feature_importance.png')
    plt.close()

    return {
        'Logistic Regression': lr_importance,
        'Random Forest': rf_importance
    }

# Hàm trực quan hóa kết quả
def visualize_results(results):
    """Trực quan hóa kết quả đánh giá mô hình"""
    # Biểu đồ ma trận nhầm lẫn
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    cm = results['Logistic Regression']['confusion_matrix']
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Ma trận nhầm lẫn - Logistic Regression')
    plt.xlabel('Dự đoán')
    plt.ylabel('Thực tế')

    plt.subplot(1, 2, 2)
    cm = results['Random Forest']['confusion_matrix']
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Ma trận nhầm lẫn - Random Forest')
    plt.xlabel('Dự đoán')
    plt.ylabel('Thực tế')

    plt.tight_layout()
    plt.savefig('confusion_matrix.png')
    plt.close()

    # Biểu đồ so sánh các chỉ số
    metrics = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
    lr_scores = [results['Logistic Regression'][m] for m in metrics]
    rf_scores = [results['Random Forest'][m] for m in metrics]

    plt.figure(figsize=(10, 6))
    x = range(len(metrics))
    width = 0.35

    plt.bar([i - width/2 for i in x], lr_scores, width, label='Logistic Regression')
    plt.bar([i + width/2 for i in x], rf_scores, width, label='Random Forest')

    plt.xlabel('Chỉ số')
    plt.ylabel('Giá trị')
    plt.title('So sánh hiệu suất mô hình')
    plt.xticks(x, metrics)
    plt.legend()

    plt.tight_layout()
    plt.savefig('model_comparison.png')
    plt.close()

# Hàm phân tích tương quan
def analyze_correlations(df):
    """Phân tích tương quan giữa các đặc trưng và biến mục tiêu"""
    # Chọn các đặc trưng số
    numeric_features = ['num_attempts', 'correct_ratio', 'time_since_last_attempt', 'days']

    if 'target' in df.columns:
        corr_features = numeric_features + ['target']
        corr_df = df[corr_features].copy()

        # Tính ma trận tương quan
        corr_matrix = corr_df.corr()

        # Trực quan hóa
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Ma trận tương quan giữa các đặc trưng')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png')
        plt.close()

        return corr_matrix

    return None

# Hàm chính
def main():
    print("Bắt đầu phân tích dữ liệu SLAM...")

    # Đọc dữ liệu
    print("Đang đọc dữ liệu huấn luyện...")
    train_instances = read_slam_file(TRAIN_PATH)
    print(f"Đã đọc {len(train_instances)} instances từ dữ liệu huấn luyện")

    print("Đang đọc dữ liệu kiểm tra...")
    dev_instances = read_slam_file(DEV_PATH)
    print(f"Đã đọc {len(dev_instances)} instances từ dữ liệu kiểm tra")

    print("Đang đọc nhãn...")
    dev_labels = read_key_file(DEV_KEY_PATH)
    print(f"Đã đọc {len(dev_labels)} nhãn")

    # Trích xuất đặc trưng
    print("Đang trích xuất đặc trưng từ dữ liệu huấn luyện...")
    train_df = extract_features(train_instances)
    print(f"Kích thước DataFrame huấn luyện: {train_df.shape}")

    print("Đang trích xuất đặc trưng từ dữ liệu kiểm tra...")
    dev_df = extract_features(dev_instances, dev_labels)
    print(f"Kích thước DataFrame kiểm tra: {dev_df.shape}")

    # Phân tích tương quan
    print("Đang phân tích tương quan...")
    corr_matrix = analyze_correlations(dev_df)

    # Chuẩn bị dữ liệu cho mô hình
    print("Đang chuẩn bị dữ liệu cho mô hình...")

    # Chọn đặc trưng và biến mục tiêu
    features = ['num_attempts', 'correct_ratio', 'time_since_last_attempt', 'days']

    # One-hot encoding cho các đặc trưng phân loại
    categorical_features = ['pos', 'format']
    for feature in categorical_features:
        dummies = pd.get_dummies(dev_df[feature], prefix=feature)
        dev_df = pd.concat([dev_df, dummies], axis=1)
        features.extend(dummies.columns.tolist())

    X = dev_df[features]
    y = dev_df['target']

    # Chia dữ liệu thành tập huấn luyện và kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Huấn luyện và đánh giá mô hình
    print("Đang huấn luyện và đánh giá mô hình...")
    results = train_and_evaluate_models(X_train, y_train, X_test, y_test)

    # In kết quả
    print("\nKết quả đánh giá mô hình:")
    for model_name, metrics in results.items():
        print(f"\n{model_name}:")
        print(f"Accuracy: {metrics['accuracy']:.4f}")
        print(f"Precision: {metrics['precision']:.4f}")
        print(f"Recall: {metrics['recall']:.4f}")
        print(f"F1 Score: {metrics['f1']:.4f}")
        print(f"ROC AUC: {metrics['roc_auc']:.4f}")

    # Phân tích tầm quan trọng của đặc trưng
    print("\nĐang phân tích tầm quan trọng của đặc trưng...")
    importance = analyze_feature_importance(results, features)

    # Trực quan hóa kết quả
    print("Đang trực quan hóa kết quả...")
    visualize_results(results)

    # Lưu mô hình
    print("Đang lưu mô hình...")
    joblib.dump(results['Logistic Regression']['model'], 'logistic_regression_model.pkl')
    joblib.dump(results['Random Forest']['model'], 'random_forest_model.pkl')

    print("\nPhân tích hoàn tất. Các biểu đồ đã được lưu.")
    print("- feature_importance.png: Biểu đồ tầm quan trọng của đặc trưng")
    print("- confusion_matrix.png: Ma trận nhầm lẫn")
    print("- model_comparison.png: So sánh hiệu suất mô hình")
    print("- correlation_matrix.png: Ma trận tương quan giữa các đặc trưng")

if __name__ == "__main__":
    main()
