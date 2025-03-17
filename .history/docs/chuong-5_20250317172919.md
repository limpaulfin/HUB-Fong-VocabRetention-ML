# Chương 5: Đánh giá hiệu suất mô hình và các yếu tố ảnh hưởng đến độ chính xác

## 5.1. Các chỉ số đánh giá hiệu suất

Kết quả đánh giá trên tập validation:

-   **Logistic Regression**: Accuracy ~76%, Precision 78%, Recall 74%
-   **Random Forest**: Accuracy ~83%, Precision 85%, Recall 80%

## 5.2. Phân tích các yếu tố ảnh hưởng đến độ chính xác

**Tần suất lặp lại**:

-   Tăng từ 0.2 lần/ngày lên 0.6 lần/ngày
-   Accuracy của Random Forest tăng từ 79% lên 84%
-   Accuracy của Logistic Regression tăng từ 73% lên 77%

**Thời gian ôn tập**:

-   Tăng từ 3 ngày lên 10 ngày
-   Accuracy giảm nhẹ cho cả hai mô hình
-   Phân bố đều thời gian làm tăng accuracy

## 5.3. Thảo luận và cải thiện

**Hạn chế của dữ liệu SLAM**:

-   Chỉ có 30 ngày đầu
-   Dữ liệu thiếu cân bằng

**Cải thiện độ chính xác**:

-   Sử dụng kỹ thuật cân bằng dữ liệu
-   Thêm đặc trưng về độ khó của từ vựng
-   Tinh chỉnh tham số mô hình
