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

Copyright © 2024 Lâm Thanh Phong - 020201240024 - Học viên cao học HUB
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import roc_curve, precision_recall_curve, auc
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap

# Đường dẫn đến thư mục kết quả
RESULTS_DIR = "../results"

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

    # Tính toán ROC curve cho Logistic Regression
    lr_fpr, lr_tpr, _ = roc_curve(y_true, lr_probs)
    lr_auc = auc(lr_fpr, lr_tpr)

    # Tính toán ROC curve cho Random Forest
    rf_fpr, rf_tpr, _ = roc_curve(y_true, rf_probs)
    rf_auc = auc(rf_fpr, rf_tpr)

    # Vẽ đường cơ sở
    plt.plot([0, 1], [0, 1], 'k--', label='Baseline')

    # Vẽ ROC curve cho Logistic Regression
    plt.plot(lr_fpr, lr_tpr, label=f'Logistic Regression (AUC = {lr_auc:.3f})')

    # Vẽ ROC curve cho Random Forest
    plt.plot(rf_fpr, rf_tpr, label=f'Random Forest (AUC = {rf_auc:.3f})')

    # Cấu hình biểu đồ
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # Lưu biểu đồ
    plt.savefig(os.path.join(RESULTS_DIR, 'roc_curves.png'))
    plt.close()

    print(f"Đã lưu biểu đồ ROC tại: {os.path.join(RESULTS_DIR, 'roc_curves.png')}")

# Hàm tạo biểu đồ Precision-Recall
def plot_precision_recall_curves(y_true, lr_probs, rf_probs):
    """Tạo biểu đồ Precision-Recall cho các mô hình"""
    plt.figure(figsize=(10, 8))

    # Tính toán Precision-Recall curve cho Logistic Regression
    lr_precision, lr_recall, _ = precision_recall_curve(y_true, lr_probs)
    lr_auc = auc(lr_recall, lr_precision)

    # Tính toán Precision-Recall curve cho Random Forest
    rf_precision, rf_recall, _ = precision_recall_curve(y_true, rf_probs)
    rf_auc = auc(rf_recall, rf_precision)

    # Vẽ đường cơ sở
    plt.plot([0, 1], [sum(y_true)/len(y_true), sum(y_true)/len(y_true)], 'k--', label='Baseline')

    # Vẽ Precision-Recall curve cho Logistic Regression
    plt.plot(lr_recall, lr_precision, label=f'Logistic Regression (AUC = {lr_auc:.3f})')

    # Vẽ Precision-Recall curve cho Random Forest
    plt.plot(rf_recall, rf_precision, label=f'Random Forest (AUC = {rf_auc:.3f})')

    # Cấu hình biểu đồ
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # Lưu biểu đồ
    plt.savefig(os.path.join(RESULTS_DIR, 'precision_recall_curves.png'))
    plt.close()

    print(f"Đã lưu biểu đồ Precision-Recall tại: {os.path.join(RESULTS_DIR, 'precision_recall_curves.png')}")

# Hàm tạo biểu đồ phân phối xác suất dự đoán
def plot_probability_distributions(y_true, lr_probs, rf_probs):
    """Tạo biểu đồ phân phối xác suất dự đoán"""
    plt.figure(figsize=(12, 10))

    # Tạo DataFrame cho biểu đồ
    df = pd.DataFrame({
        'True Label': y_true,
        'Logistic Regression': lr_probs,
        'Random Forest': rf_probs
    })

    # Biểu đồ phân phối xác suất cho Logistic Regression
    plt.subplot(2, 1, 1)
    sns.histplot(data=df, x='Logistic Regression', hue='True Label', bins=30, kde=True, palette='coolwarm')
    plt.title('Phân phối xác suất dự đoán - Logistic Regression')
    plt.xlabel('Xác suất dự đoán')
    plt.ylabel('Số lượng')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Biểu đồ phân phối xác suất cho Random Forest
    plt.subplot(2, 1, 2)
    sns.histplot(data=df, x='Random Forest', hue='True Label', bins=30, kde=True, palette='coolwarm')
    plt.title('Phân phối xác suất dự đoán - Random Forest')
    plt.xlabel('Xác suất dự đoán')
    plt.ylabel('Số lượng')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()

    # Lưu biểu đồ
    plt.savefig(os.path.join(RESULTS_DIR, 'probability_distributions.png'))
    plt.close()

    print(f"Đã lưu biểu đồ phân phối xác suất tại: {os.path.join(RESULTS_DIR, 'probability_distributions.png')}")

# Hàm tạo biểu đồ tổng hợp
def create_dashboard(y_true, lr_probs, rf_probs, feature_importance):
    """Tạo dashboard tổng hợp các biểu đồ"""
    plt.figure(figsize=(20, 15))
    gs = gridspec.GridSpec(2, 2)

    # Biểu đồ ROC
    ax1 = plt.subplot(gs[0, 0])

    # Tính toán ROC curve cho Logistic Regression
    lr_fpr, lr_tpr, _ = roc_curve(y_true, lr_probs)
    lr_auc = auc(lr_fpr, lr_tpr)

    # Tính toán ROC curve cho Random Forest
    rf_fpr, rf_tpr, _ = roc_curve(y_true, rf_probs)
    rf_auc = auc(rf_fpr, rf_tpr)

    # Vẽ đường cơ sở
    ax1.plot([0, 1], [0, 1], 'k--', label='Baseline')

    # Vẽ ROC curve cho Logistic Regression
    ax1.plot(lr_fpr, lr_tpr, label=f'Logistic Regression (AUC = {lr_auc:.3f})')

    # Vẽ ROC curve cho Random Forest
    ax1.plot(rf_fpr, rf_tpr, label=f'Random Forest (AUC = {rf_auc:.3f})')

    # Cấu hình biểu đồ
    ax1.set_xlabel('False Positive Rate')
    ax1.set_ylabel('True Positive Rate')
    ax1.set_title('ROC Curve')
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.7)

    # Biểu đồ Precision-Recall
    ax2 = plt.subplot(gs[0, 1])

    # Tính toán Precision-Recall curve cho Logistic Regression
    lr_precision, lr_recall, _ = precision_recall_curve(y_true, lr_probs)
    lr_pr_auc = auc(lr_recall, lr_precision)

    # Tính toán Precision-Recall curve cho Random Forest
    rf_precision, rf_recall, _ = precision_recall_curve(y_true, rf_probs)
    rf_pr_auc = auc(rf_recall, rf_precision)

    # Vẽ đường cơ sở
    ax2.plot([0, 1], [sum(y_true)/len(y_true), sum(y_true)/len(y_true)], 'k--', label='Baseline')

    # Vẽ Precision-Recall curve cho Logistic Regression
    ax2.plot(lr_recall, lr_precision, label=f'Logistic Regression (AUC = {lr_pr_auc:.3f})')

    # Vẽ Precision-Recall curve cho Random Forest
    ax2.plot(rf_recall, rf_precision, label=f'Random Forest (AUC = {rf_pr_auc:.3f})')

    # Cấu hình biểu đồ
    ax2.set_xlabel('Recall')
    ax2.set_ylabel('Precision')
    ax2.set_title('Precision-Recall Curve')
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.7)

    # Biểu đồ tầm quan trọng của đặc trưng
    ax3 = plt.subplot(gs[1, 0])

    # Vẽ biểu đồ tầm quan trọng của đặc trưng
    top_features = feature_importance.head(10)
    sns.barplot(x='Importance', y='Feature', data=top_features, ax=ax3)
    ax3.set_title('Top 10 đặc trưng quan trọng nhất')
    ax3.set_xlabel('Tầm quan trọng')
    ax3.set_ylabel('Đặc trưng')
    ax3.grid(True, linestyle='--', alpha=0.7)

    # Biểu đồ phân phối xác suất
    ax4 = plt.subplot(gs[1, 1])

    # Tạo DataFrame cho biểu đồ
    df = pd.DataFrame({
        'True Label': y_true,
        'Logistic Regression': lr_probs,
        'Random Forest': rf_probs
    })

    # Biểu đồ phân phối xác suất
    for label in [0, 1]:
        subset = df[df['True Label'] == label]
        ax4.hist(subset['Random Forest'], bins=20, alpha=0.5, label=f'True Label = {label}')

    ax4.set_title('Phân phối xác suất dự đoán - Random Forest')
    ax4.set_xlabel('Xác suất dự đoán')
    ax4.set_ylabel('Số lượng')
    ax4.legend()
    ax4.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()

    # Lưu biểu đồ
    plt.savefig(os.path.join(RESULTS_DIR, 'dashboard.png'))
    plt.close()

    print(f"Đã tạo dashboard tại: {os.path.join(RESULTS_DIR, 'dashboard.png')}")

# Hàm tạo biểu đồ 3D để phân tích mối quan hệ giữa các đặc trưng
def plot_3d_feature_relationships(X, y, feature_names):
    """Tạo biểu đồ 3D để phân tích mối quan hệ giữa các đặc trưng"""
    from mpl_toolkits.mplot3d import Axes3D

    # Chọn 3 đặc trưng quan trọng nhất
    top_features = feature_names[:3]

    # Tạo biểu đồ 3D
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Tạo colormap
    cmap = LinearSegmentedColormap.from_list('custom_cmap', ['blue', 'red'])

    # Vẽ điểm dữ liệu
    scatter = ax.scatter(
        X[top_features[0]],
        X[top_features[1]],
        X[top_features[2]],
        c=y,
        cmap=cmap,
        s=50,
        alpha=0.6
    )

    # Cấu hình biểu đồ
    ax.set_xlabel(top_features[0])
    ax.set_ylabel(top_features[1])
    ax.set_zlabel(top_features[2])
    ax.set_title('Mối quan hệ 3D giữa các đặc trưng quan trọng nhất')

    # Thêm colorbar
    cbar = plt.colorbar(scatter)
    cbar.set_label('Nhãn (0: Quên, 1: Nhớ)')

    # Lưu biểu đồ
    plt.savefig(os.path.join(RESULTS_DIR, '3d_feature_relationships.png'))
    plt.close()

    print(f"Đã lưu biểu đồ 3D tại: {os.path.join(RESULTS_DIR, '3d_feature_relationships.png')}")

# Hàm chính
def main():
    """Hàm chính để trực quan hóa kết quả"""
    print("Bắt đầu trực quan hóa kết quả...")

    # Tải mô hình
    lr_model, rf_model = load_models()

    if lr_model is None or rf_model is None:
        return

    # Tạo dữ liệu mẫu để trực quan hóa
    # Trong thực tế, bạn nên sử dụng dữ liệu kiểm tra thực tế
    print("Tạo dữ liệu mẫu để trực quan hóa...")
    np.random.seed(42)
    n_samples = 1000

    # Tạo đặc trưng
    X = pd.DataFrame({
        'num_attempts': np.random.randint(0, 10, n_samples),
        'correct_ratio': np.random.random(n_samples),
        'time_since_last_attempt': np.random.exponential(5, n_samples),
        'days': np.random.uniform(0, 30, n_samples)
    })

    # Thêm một số đặc trưng phân loại
    pos_categories = ['NOUN', 'VERB', 'ADJ', 'ADV', 'PRON']
    format_categories = ['reverse_translate', 'reverse_tap', 'listen', 'select']

    for pos in pos_categories:
        X[f'pos_{pos}'] = np.random.randint(0, 2, n_samples)

    for format_type in format_categories:
        X[f'format_{format_type}'] = np.random.randint(0, 2, n_samples)

    # Tạo nhãn thực tế
    y = np.random.randint(0, 2, n_samples)

    # Dự đoán xác suất
    lr_probs = lr_model.predict_proba(X)[:, 1]
    rf_probs = rf_model.predict_proba(X)[:, 1]

    # Tạo DataFrame tầm quan trọng của đặc trưng
    feature_names = X.columns.tolist()

    # Lấy tầm quan trọng của đặc trưng từ Random Forest
    rf_importance = rf_model.named_steps['model'].feature_importances_

    feature_importance = pd.DataFrame({
        'Feature': feature_names,
        'Importance': rf_importance
    }).sort_values('Importance', ascending=False)

    # Tạo các biểu đồ
    print("Đang tạo các biểu đồ...")
    plot_roc_curves(y, lr_probs, rf_probs)
    plot_precision_recall_curves(y, lr_probs, rf_probs)
    plot_probability_distributions(y, lr_probs, rf_probs)
    create_dashboard(y, lr_probs, rf_probs, feature_importance)
    plot_3d_feature_relationships(X, y, feature_importance['Feature'].tolist())

    print("\nTrực quan hóa hoàn tất. Các biểu đồ đã được lưu trong thư mục:", RESULTS_DIR)

if __name__ == "__main__":
    main()
