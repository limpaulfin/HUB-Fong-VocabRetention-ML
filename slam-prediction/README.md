# Phân tích dữ liệu SLAM và dự đoán khả năng ghi nhớ từ vựng

Dự án này phân tích dữ liệu SLAM (Second Language Acquisition Modeling) của Duolingo để dự đoán khả năng ghi nhớ từ vựng của người học dựa trên hành vi học tập.

## Cấu trúc dự án

```
slam-prediction/
├── code/                          # Thư mục chứa mã nguồn
│   ├── slam_analysis.py           # Script phân tích chính
│   └── visualize_results.py       # Script trực quan hóa kết quả
│
├── data/                          # Thư mục chứa dữ liệu
│   └── dataverse_files/           # Cấu trúc thư mục cho dữ liệu SLAM
│       ├── data_en_es.tar/        # Cấu trúc thư mục cho dữ liệu tiếng Anh-Tây Ban Nha
│       ├── data_es_en.tar/        # Cấu trúc thư mục cho dữ liệu tiếng Tây Ban Nha-Anh
│       ├── data_fr_en.tar/        # Cấu trúc thư mục cho dữ liệu tiếng Pháp-Anh
│       └── starter_code.tar/      # Mã khởi động từ Duolingo
│
├── results/                       # Thư mục chứa kết quả phân tích (sẽ được tạo)
│   ├── feature_importance.png     # Biểu đồ tầm quan trọng của đặc trưng
│   ├── confusion_matrix.png       # Ma trận nhầm lẫn
│   ├── model_comparison.png       # So sánh hiệu suất mô hình
│   ├── correlation_matrix.png     # Ma trận tương quan giữa các đặc trưng
│   ├── roc_curves.png             # Biểu đồ ROC
│   ├── precision_recall_curves.png # Biểu đồ Precision-Recall
│   ├── probability_distributions.png # Phân phối xác suất dự đoán
│   ├── dashboard.png              # Dashboard tổng hợp
│   ├── 3d_feature_relationships.png # Mối quan hệ 3D giữa các đặc trưng
│   ├── analysis_report.md         # Báo cáo phân tích
│   ├── logistic_regression_model.pkl # Mô hình Logistic Regression đã huấn luyện
│   └── random_forest_model.pkl    # Mô hình Random Forest đã huấn luyện
│
└── README.md                      # File này
```

## Yêu cầu

Để chạy mã phân tích, bạn cần cài đặt các thư viện Python sau:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

## Tải dữ liệu SLAM

**Lưu ý quan trọng**: Các file dữ liệu lớn không được lưu trữ trong repository này do giới hạn kích thước của GitHub. Bạn cần tải dữ liệu SLAM từ trang Dataverse của Duolingo và đặt vào cấu trúc thư mục tương ứng.

### Các bước tải dữ liệu:

1. Truy cập trang web Dataverse của Duolingo SLAM: [https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/8SWHNO](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/8SWHNO)

2. Tải xuống các file dữ liệu sau:

    - `data_en_es.tar`
    - `data_es_en.tar`
    - `data_fr_en.tar`
    - `starter_code.tar`

3. Giải nén các file tar vào cấu trúc thư mục tương ứng trong `slam-prediction/data/dataverse_files/`:
    - Giải nén `data_en_es.tar` vào thư mục `data_en_es.tar/`
    - Giải nén `data_es_en.tar` vào thư mục `data_es_en.tar/`
    - Giải nén `data_fr_en.tar` vào thư mục `data_fr_en.tar/`
    - Giải nén `starter_code.tar` vào thư mục `starter_code.tar/`

## Các bước thực hiện

### 1. Chạy phân tích dữ liệu

Sau khi tải và giải nén dữ liệu vào cấu trúc thư mục thích hợp, chạy script phân tích:

```bash
cd slam-prediction/code
python slam_analysis.py
```

Script này sẽ:

-   Đọc dữ liệu SLAM từ thư mục `data/dataverse_files`
-   Trích xuất đặc trưng từ dữ liệu
-   Huấn luyện và đánh giá các mô hình Logistic Regression và Random Forest
-   Tạo các biểu đồ và báo cáo phân tích
-   Lưu kết quả vào thư mục `results`

### 2. Trực quan hóa kết quả

Sau khi phân tích dữ liệu, bạn có thể tạo thêm các biểu đồ trực quan hóa:

```bash
cd slam-prediction/code
python visualize_results.py
```

Script này sẽ:

-   Tải các mô hình đã huấn luyện
-   Tạo các biểu đồ ROC, Precision-Recall
-   Tạo biểu đồ phân phối xác suất dự đoán
-   Tạo dashboard tổng hợp
-   Tạo biểu đồ 3D để phân tích mối quan hệ giữa các đặc trưng

## Kết quả

Sau khi chạy các script, các kết quả sau sẽ được tạo ra trong thư mục `results`:

1. **Biểu đồ tầm quan trọng của đặc trưng** (`feature_importance.png`): Hiển thị các đặc trưng quan trọng nhất ảnh hưởng đến việc dự đoán khả năng ghi nhớ từ vựng.

2. **Ma trận nhầm lẫn** (`confusion_matrix.png`): Hiển thị hiệu suất của mô hình trong việc phân loại các trường hợp ghi nhớ và quên từ vựng.

3. **So sánh hiệu suất mô hình** (`model_comparison.png`): So sánh hiệu suất của các mô hình Logistic Regression và Random Forest dựa trên các chỉ số như accuracy, precision, recall, F1 và ROC AUC.

4. **Ma trận tương quan** (`correlation_matrix.png`): Hiển thị mối tương quan giữa các đặc trưng và biến mục tiêu.

5. **Biểu đồ ROC** (`roc_curves.png`): Hiển thị đường cong ROC của các mô hình.

6. **Biểu đồ Precision-Recall** (`precision_recall_curves.png`): Hiển thị đường cong Precision-Recall của các mô hình.

7. **Phân phối xác suất dự đoán** (`probability_distributions.png`): Hiển thị phân phối xác suất dự đoán của các mô hình.

8. **Dashboard tổng hợp** (`dashboard.png`): Tổng hợp các biểu đồ quan trọng trong một dashboard.

9. **Mối quan hệ 3D giữa các đặc trưng** (`3d_feature_relationships.png`): Hiển thị mối quan hệ 3D giữa các đặc trưng quan trọng nhất.

10. **Báo cáo phân tích** (`analysis_report.md`): Báo cáo chi tiết về kết quả phân tích, bao gồm:

    - Kết quả đánh giá mô hình
    - Tầm quan trọng của đặc trưng
    - Tương quan giữa các đặc trưng
    - Kết luận

11. **Mô hình đã huấn luyện**: Các mô hình được lưu dưới dạng file pickle (`logistic_regression_model.pkl` và `random_forest_model.pkl`).

## Giải thích các đặc trưng

Các đặc trưng chính được sử dụng trong mô hình:

-   **num_attempts**: Số lần người dùng đã thử từ vựng này
-   **correct_ratio**: Tỷ lệ đúng của người dùng với từ vựng này
-   **time_since_last_attempt**: Thời gian kể từ lần thử gần nhất
-   **days**: Số ngày kể từ khi người dùng bắt đầu học
-   **pos**: Loại từ (danh từ, động từ, v.v.)
-   **format**: Định dạng bài tập (reverse_translate, reverse_tap, v.v.)

## Giải thích kết quả

Kết quả phân tích cho thấy:

1. **Tầm quan trọng của đặc trưng**:

    - Theo Logistic Regression: format_reverse_tap (0.4478), num_attempts (0.3922), format_listen (0.2850), và correct_ratio (0.2009) là các đặc trưng quan trọng nhất.
    - Theo Random Forest: num_attempts (0.2059), format_reverse_tap (0.2054), correct_ratio (0.1626), và format_listen (0.1100) là các đặc trưng quan trọng nhất.

2. **Hiệu suất mô hình**:

    - Cả hai mô hình đều đạt hiệu suất tốt với độ chính xác khoảng 85.8%.
    - Random Forest có hiệu suất nhỉnh hơn một chút (85.82%) so với Logistic Regression (85.80%).
    - Mô hình Random Forest có precision cao hơn (0.8750 so với 0.5000), nhưng cả hai mô hình đều có recall thấp (khoảng 0.002).

3. **Tương quan**:
    - Tương quan với biến mục tiêu (khả năng ghi nhớ từ vựng):
        - correct_ratio: 0.08 (tương quan dương)
        - days: 0.00 (không có tương quan)
        - time_since_last_attempt: -0.02 (tương quan âm yếu)
        - num_attempts: -0.09 (tương quan âm)

## Lưu ý

-   Quá trình phân tích có thể mất một thời gian do kích thước lớn của dữ liệu SLAM.
-   Đảm bảo có đủ dung lượng ổ đĩa, vì dữ liệu SLAM và kết quả phân tích có thể chiếm nhiều không gian.
-   Các file dữ liệu lớn (như `en_es.slam.20190204.train`, `en_es.slam.20190204.dev`, v.v.) không được lưu trữ trong repository này nhưng cần thiết để chạy mã phân tích. Hãy tải chúng từ nguồn được đề cập ở trên.
