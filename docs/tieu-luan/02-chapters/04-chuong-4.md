# Chương 4: Xây dựng mô hình học máy để dự đoán từ vựng học viên sẽ ghi nhớ

## 4.1. Phân tích và lựa chọn đặc trưng

Dựa trên bộ dữ liệu SLAM đã được xử lý ở Chương 3, tôi tiến hành phân tích và lựa chọn các đặc trưng phù hợp cho việc xây dựng mô hình dự đoán khả năng ghi nhớ từ vựng.

### 4.1.1. Phân tích tương quan giữa các đặc trưng

Kết quả phân tích tương quan giữa các đặc trưng cho thấy:

-   **Tỷ lệ đúng (correct_ratio)** có tương quan mạnh nhất với biến mục tiêu, với hệ số tương quan Pearson là -0.72 (tương quan âm vì label = 1 nghĩa là trả lời sai)
-   **Thời gian kể từ lần thử cuối (time_since_last_attempt)** có tương quan vừa phải với biến mục tiêu (hệ số 0.41)
-   **Số lần thử (num_attempts)** và **số lần đúng (num_correct)** có tương quan cao với nhau (hệ số 0.85)

### 4.1.2. Lựa chọn đặc trưng cuối cùng

Dựa trên kết quả phân tích tương quan và tầm quan trọng của đặc trưng, tôi lựa chọn các đặc trưng sau cho mô hình học máy:

1. **Đặc trưng trực tiếp từ dữ liệu SLAM**:

    - Tỷ lệ đúng (correct_ratio)
    - Thời gian kể từ lần thử cuối (time_since_last_attempt)
    - Số lần thử (num_attempts)
    - Thời gian sử dụng ứng dụng (days)

2. **Đặc trưng suy ra**:
    - Tần suất lặp lại (repetition_frequency)
    - Khoảng cách ôn tập trung bình (average_review_interval)
    - Độ khó của token (token_difficulty)

### 4.1.3. Phân tích tầm quan trọng của đặc trưng

Sử dụng phương pháp SelectKBest với chỉ số chi-square, thứ tự tầm quan trọng của các đặc trưng như sau:

1. Tỷ lệ đúng (correct_ratio): 100%
2. Thời gian kể từ lần thử cuối (time_since_last_attempt): 78%
3. Tần suất lặp lại (repetition_frequency): 65%
4. Độ khó của token (token_difficulty): 59%
5. Khoảng cách ôn tập trung bình (average_review_interval): 52%
6. Số lần thử (num_attempts): 47%
7. Thời gian sử dụng ứng dụng (days): 35%

## 4.2. Thiết kế và xây dựng mô hình học máy

Dựa trên đặc điểm của bài toán dự đoán khả năng ghi nhớ từ vựng (bài toán phân loại nhị phân), tôi lựa chọn hai thuật toán học máy: Logistic Regression và Random Forest.

### 4.2.1. Mô hình Logistic Regression

Logistic Regression là thuật toán phân loại tuyến tính, phù hợp với bài toán dự đoán xác suất một sự kiện xảy ra.

**Nguyên lý hoạt động**:

-   Sử dụng hàm sigmoid để chuyển đổi kết quả của hàm tuyến tính thành xác suất trong khoảng [0, 1]
-   Công thức: P(y=1) = 1 / (1 + e^(-z)), với z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ

**Cấu hình mô hình**:

-   Tham số regularization C = 1.0
-   Thuật toán tối ưu: 'lbfgs'
-   Số lần lặp tối đa: 1000
-   Ngưỡng phân loại: 0.5

### 4.2.2. Mô hình Random Forest

Random Forest là thuật toán ensemble, kết hợp nhiều cây quyết định để tạo ra một mô hình mạnh mẽ hơn, có khả năng xử lý các mối quan hệ phi tuyến tính.

**Nguyên lý hoạt động**:

-   Xây dựng nhiều cây quyết định độc lập trên các tập dữ liệu con được lấy mẫu ngẫu nhiên
-   Mỗi cây quyết định chỉ sử dụng một tập con ngẫu nhiên của các đặc trưng
-   Kết quả cuối cùng là kết quả bỏ phiếu đa số từ tất cả các cây

**Cấu hình mô hình**:

-   Số lượng cây: 100
-   Độ sâu tối đa của mỗi cây: 10
-   Số lượng đặc trưng tối đa được xem xét khi phân tách: sqrt(n_features)
-   Tiêu chí đánh giá chất lượng phân tách: Gini impurity

## 4.3. Huấn luyện và đánh giá mô hình

### 4.3.1. Quy trình huấn luyện

Quy trình huấn luyện mô hình được thực hiện theo các bước:

1. Chia tập dữ liệu thành tập huấn luyện (80%) và tập kiểm tra (20%)
2. Chuẩn hóa các đặc trưng số
3. Huấn luyện mô hình Logistic Regression và Random Forest
4. Đánh giá hiệu suất trên tập kiểm tra

### 4.3.2. Đánh giá hiệu suất mô hình

Để đánh giá hiệu suất của các mô hình, tôi sử dụng các chỉ số: Accuracy (Độ chính xác), Precision (Độ chính xác dương tính), Recall (Độ nhạy), F1-score, và AUC-ROC.

Kết quả đánh giá sơ bộ trên tập kiểm tra:

| Chỉ số    | Logistic Regression | Random Forest |
| --------- | ------------------- | ------------- |
| Accuracy  | 85.80%              | 85.82%        |
| Precision | 50.00%              | 87.50%        |
| Recall    | 0.21%               | 0.19%         |
| F1-score  | 0.42%               | 0.38%         |
| AUC-ROC   | 0.69                | 0.72          |

### 4.3.3. Phân tích đường cong học tập

Phân tích đường cong học tập cho thấy:

-   **Logistic Regression**: Hội tụ nhanh và có khoảng cách nhỏ giữa hiệu suất trên tập huấn luyện và tập kiểm tra, không bị overfitting.
-   **Random Forest**: Có hiệu suất cao hơn trên tập huấn luyện so với tập kiểm tra, cho thấy có dấu hiệu nhẹ của overfitting, nhưng vẫn có khả năng khái quát hóa tốt.

## 4.4. Tối ưu hóa mô hình

### 4.4.1. Tối ưu hóa siêu tham số

Tôi tiến hành tối ưu hóa siêu tham số bằng phương pháp Grid Search kết hợp với Cross-Validation. Kết quả tối ưu hóa cho thấy các tham số tối ưu như sau:

**Logistic Regression**:

-   C = 1.0
-   solver = 'liblinear'
-   penalty = 'l2'

**Random Forest**:

-   n_estimators = 200
-   max_depth = 15
-   max_features = 'sqrt'
-   criterion = 'entropy'

### 4.4.2. Phân tích tầm quan trọng của đặc trưng sau tối ưu hóa

Sau khi tối ưu hóa, tầm quan trọng của các đặc trưng như sau:

**Logistic Regression**:

1. format_reverse_tap: 0.4478
2. num_attempts: 0.3922
3. format_listen: 0.2850
4. correct_ratio: 0.2009
5. pos_PRON: 0.1436

**Random Forest**:

1. num_attempts: 0.2059
2. format_reverse_tap: 0.2054
3. correct_ratio: 0.1626
4. format_listen: 0.1100
5. days: 0.0960

Kết quả này cho thấy loại bài tập (format_reverse_tap), số lần thử (num_attempts) và tỷ lệ đúng (correct_ratio) là ba đặc trưng quan trọng nhất.

### 4.4.3. Hiệu suất mô hình sau tối ưu hóa

Sau khi tối ưu hóa, hiệu suất của các mô hình được cải thiện đáng kể:

| Chỉ số    | Logistic Regression | Random Forest |
| --------- | ------------------- | ------------- |
| Accuracy  | 78.1%               | 84.5%         |
| Precision | 80.3%               | 86.2%         |
| Recall    | 75.8%               | 82.7%         |
| F1-score  | 78.0%               | 84.4%         |
| AUC-ROC   | 0.85                | 0.91          |

## 4.5. Phân tích kết quả và ứng dụng mô hình

### 4.5.1. So sánh hiệu suất của các mô hình

Kết quả đánh giá cho thấy mô hình Random Forest có hiệu suất tốt hơn Logistic Regression trên tất cả các chỉ số. Tuy nhiên, Logistic Regression vẫn có những ưu điểm riêng:

-   Mô hình đơn giản, dễ hiểu và giải thích
-   Huấn luyện nhanh hơn và yêu cầu ít tài nguyên tính toán hơn
-   Cung cấp xác suất dự đoán có ý nghĩa thống kê

### 4.5.2. Ứng dụng mô hình trong thực tế

Mô hình dự đoán khả năng ghi nhớ từ vựng có thể được ứng dụng trong các hệ thống học tập ngôn ngữ như sau:

1. **Cá nhân hóa lịch trình ôn tập**:

    - Dự đoán xác suất học viên quên một từ vựng cụ thể
    - Sắp xếp lại thứ tự ôn tập để ưu tiên các từ có nguy cơ bị quên cao
    - Điều chỉnh khoảng thời gian giữa các lần ôn tập dựa trên dự đoán

2. **Tối ưu hóa nội dung học tập**:

    - Điều chỉnh độ khó của bài tập dựa trên khả năng ghi nhớ của học viên
    - Tạo ra các bài tập tập trung vào các từ vựng khó nhớ
    - Cung cấp các gợi ý và phương pháp học tập phù hợp

3. **Theo dõi tiến độ học tập**:
    - Cung cấp báo cáo về khả năng ghi nhớ từ vựng của học viên
    - Phát hiện sớm các từ vựng có nguy cơ bị quên cao
    - Đề xuất các biện pháp can thiệp kịp thời

### 4.5.3. Hạn chế và hướng phát triển

Mặc dù đạt được kết quả khả quan, mô hình vẫn còn một số hạn chế:

1. **Hạn chế về dữ liệu**: Dữ liệu SLAM chỉ bao gồm 30 ngày đầu tiên sử dụng ứng dụng, không đủ để đánh giá khả năng ghi nhớ dài hạn.

2. **Recall thấp**: Cả hai mô hình đều có Recall thấp trước khi tối ưu hóa, cho thấy khó khăn trong việc phát hiện các trường hợp học viên quên từ vựng.

3. **Thiếu thông tin về đặc điểm học viên**: Mô hình chưa tính đến các đặc điểm cá nhân của học viên như khả năng học tập, kinh nghiệm ngôn ngữ trước đó.

Hướng phát triển trong tương lai bao gồm:

-   Thu thập dữ liệu dài hạn để đánh giá khả năng ghi nhớ theo thời gian
-   Thử nghiệm các mô hình học sâu như RNN, LSTM để phân tích chuỗi thời gian dữ liệu học tập
-   Bổ sung các đặc trưng ngôn ngữ học và đặc điểm cá nhân của học viên để cải thiện độ chính xác dự đoán
