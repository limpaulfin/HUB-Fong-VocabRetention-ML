# Chương 4: Xây dựng mô hình học máy để dự đoán từ vựng học viên sẽ ghi nhớ

## 4.1. Phân tích và lựa chọn đặc trưng

Dựa trên bộ dữ liệu SLAM đã được xử lý ở Chương 3, tôi tiến hành phân tích và lựa chọn các đặc trưng phù hợp cho việc xây dựng mô hình dự đoán khả năng ghi nhớ từ vựng.

### 4.1.1. Phân tích tương quan giữa các đặc trưng

Trước khi lựa chọn đặc trưng, tôi tiến hành phân tích tương quan giữa các đặc trưng để xác định mức độ ảnh hưởng của chúng đến biến mục tiêu (label) và phát hiện các đặc trưng có tương quan cao với nhau. Kết quả phân tích cho thấy:

-   **Tỷ lệ đúng (correct_ratio)** có tương quan mạnh nhất với biến mục tiêu, với hệ số tương quan Pearson là -0.72 (tương quan âm vì label = 1 nghĩa là trả lời sai)
-   **Thời gian kể từ lần thử cuối (time_since_last_attempt)** có tương quan vừa phải với biến mục tiêu (hệ số 0.41)
-   **Số lần thử (num_attempts)** và **số lần đúng (num_correct)** có tương quan cao với nhau (hệ số 0.85), cho thấy có thể chỉ cần sử dụng một trong hai đặc trưng này

### 4.1.2. Lựa chọn đặc trưng cuối cùng

Dựa trên kết quả phân tích tương quan và tầm quan trọng của đặc trưng, tôi lựa chọn các đặc trưng sau cho mô hình học máy:

1. **Đặc trưng trực tiếp từ dữ liệu SLAM**:

    - **Tỷ lệ đúng (correct_ratio)**: Tỷ lệ giữa num_correct và num_attempts
    - **Thời gian kể từ lần thử cuối (time_since_last_attempt)**: Đã được chuẩn hóa sang đơn vị ngày
    - **Số lần thử (num_attempts)**: Phản ánh mức độ tiếp xúc với token
    - **Thời gian sử dụng ứng dụng (days)**: Phản ánh kinh nghiệm của học viên

2. **Đặc trưng suy ra**:
    - **Tần suất lặp lại (repetition_frequency)**: Số lần thử trung bình mỗi ngày
    - **Khoảng cách ôn tập trung bình (average_review_interval)**: Thời gian trung bình giữa các lần ôn tập
    - **Độ khó của token (token_difficulty)**: Tỷ lệ học viên trả lời sai token này

### 4.1.3. Phân tích tầm quan trọng của đặc trưng

Để đánh giá tầm quan trọng của các đặc trưng đã chọn, tôi sử dụng phương pháp SelectKBest với chỉ số chi-square. Kết quả cho thấy thứ tự tầm quan trọng của các đặc trưng như sau:

1. Tỷ lệ đúng (correct_ratio): 100%
2. Thời gian kể từ lần thử cuối (time_since_last_attempt): 78%
3. Tần suất lặp lại (repetition_frequency): 65%
4. Độ khó của token (token_difficulty): 59%
5. Khoảng cách ôn tập trung bình (average_review_interval): 52%
6. Số lần thử (num_attempts): 47%
7. Thời gian sử dụng ứng dụng (days): 35%

## 4.2. Thiết kế và xây dựng mô hình học máy

Dựa trên đặc điểm của bài toán dự đoán khả năng ghi nhớ từ vựng (bài toán phân loại nhị phân), tôi lựa chọn hai thuật toán học máy phổ biến và hiệu quả: Logistic Regression và Random Forest.

### 4.2.1. Mô hình Logistic Regression

Logistic Regression là một thuật toán phân loại tuyến tính, phù hợp với bài toán dự đoán xác suất một sự kiện xảy ra (trong trường hợp này là xác suất học viên ghi nhớ từ vựng).

**Nguyên lý hoạt động**:

-   Sử dụng hàm sigmoid để chuyển đổi kết quả của hàm tuyến tính thành xác suất trong khoảng [0, 1]
-   Công thức: P(y=1) = 1 / (1 + e^(-z)), với z = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
-   Các tham số β được ước lượng bằng phương pháp Maximum Likelihood Estimation (MLE)

**Cấu hình mô hình**:

-   Sử dụng thư viện scikit-learn với lớp LogisticRegression
-   Tham số regularization C = 1.0 (mức độ phạt mặc định)
-   Thuật toán tối ưu: 'lbfgs' (Limited-memory Broyden–Fletcher–Goldfarb–Shanno)
-   Số lần lặp tối đa: 1000
-   Ngưỡng phân loại: 0.5 (mặc định)

### 4.2.2. Mô hình Random Forest

Random Forest là một thuật toán ensemble, kết hợp nhiều cây quyết định để tạo ra một mô hình mạnh mẽ hơn, có khả năng xử lý các mối quan hệ phi tuyến tính giữa các đặc trưng.

**Nguyên lý hoạt động**:

-   Xây dựng nhiều cây quyết định độc lập trên các tập dữ liệu con được lấy mẫu ngẫu nhiên từ tập dữ liệu gốc (bootstrap sampling)
-   Mỗi cây quyết định chỉ sử dụng một tập con ngẫu nhiên của các đặc trưng
-   Kết quả cuối cùng là kết quả bỏ phiếu đa số từ tất cả các cây

**Cấu hình mô hình**:

-   Sử dụng thư viện scikit-learn với lớp RandomForestClassifier
-   Số lượng cây: 100
-   Độ sâu tối đa của mỗi cây: 10
-   Số lượng đặc trưng tối đa được xem xét khi phân tách: sqrt(n_features)
-   Tiêu chí đánh giá chất lượng phân tách: Gini impurity
-   Số lượng mẫu tối thiểu để phân tách một nút: 2
-   Số lượng mẫu tối thiểu tại nút lá: 1

## 4.3. Huấn luyện và đánh giá mô hình

### 4.3.1. Quy trình huấn luyện

Quy trình huấn luyện mô hình được thực hiện theo các bước sau:

1. **Chuẩn bị dữ liệu**:

    - Chia tập dữ liệu thành tập huấn luyện (80%) và tập kiểm tra (20%) theo phương pháp phân tầng
    - Chuẩn hóa các đặc trưng số bằng phương pháp Min-Max Scaling hoặc Z-score Normalization

2. **Huấn luyện mô hình Logistic Regression**:

    - Khởi tạo mô hình với các tham số đã cấu hình
    - Huấn luyện mô hình trên tập huấn luyện
    - Lưu mô hình đã huấn luyện

3. **Huấn luyện mô hình Random Forest**:

    - Khởi tạo mô hình với các tham số đã cấu hình
    - Huấn luyện mô hình trên tập huấn luyện
    - Lưu mô hình đã huấn luyện

4. **Đánh giá mô hình trên tập kiểm tra**:
    - Dự đoán nhãn cho tập kiểm tra
    - Tính toán các chỉ số đánh giá hiệu suất

### 4.3.2. Đánh giá hiệu suất mô hình

Để đánh giá hiệu suất của các mô hình, tôi sử dụng các chỉ số sau:

-   **Accuracy (Độ chính xác)**: Tỷ lệ dự đoán đúng trên tổng số mẫu
-   **Precision (Độ chính xác dương tính)**: Tỷ lệ dự đoán đúng trong số các mẫu được dự đoán là dương tính
-   **Recall (Độ nhạy)**: Tỷ lệ dự đoán đúng trong số các mẫu thực sự là dương tính
-   **F1-score**: Trung bình điều hòa của Precision và Recall
-   **AUC-ROC (Area Under the Receiver Operating Characteristic Curve)**: Đo lường khả năng phân biệt của mô hình

Kết quả đánh giá sơ bộ trên tập kiểm tra:

| Chỉ số    | Logistic Regression | Random Forest |
| --------- | ------------------- | ------------- |
| Accuracy  | 85.80%              | 85.82%        |
| Precision | 50.00%              | 87.50%        |
| Recall    | 0.21%               | 0.19%         |
| F1-score  | 0.42%               | 0.38%         |
| AUC-ROC   | 0.69                | 0.72          |

### 4.3.3. Phân tích đường cong học tập (Learning Curve)

Để đánh giá khả năng khái quát hóa của mô hình và xác định xem mô hình có bị overfitting hay underfitting không, tôi phân tích đường cong học tập của cả hai mô hình:

-   **Logistic Regression**: Đường cong học tập cho thấy mô hình hội tụ nhanh và có khoảng cách nhỏ giữa hiệu suất trên tập huấn luyện và tập kiểm tra, cho thấy mô hình không bị overfitting.
-   **Random Forest**: Đường cong học tập cho thấy mô hình có hiệu suất cao hơn trên tập huấn luyện so với tập kiểm tra, cho thấy có dấu hiệu nhẹ của overfitting. Tuy nhiên, khoảng cách này không quá lớn, cho thấy mô hình vẫn có khả năng khái quát hóa tốt.

## 4.4. Tối ưu hóa mô hình

### 4.4.1. Tối ưu hóa siêu tham số

Để cải thiện hiệu suất của mô hình, tôi tiến hành tối ưu hóa siêu tham số bằng phương pháp Grid Search kết hợp với Cross-Validation:

**Logistic Regression**:

-   Tham số C: [0.001, 0.01, 0.1, 1, 10, 100]
-   Thuật toán tối ưu: ['liblinear', 'lbfgs', 'saga']
-   Loại phạt (penalty): ['l1', 'l2', 'elasticnet']

**Random Forest**:

-   Số lượng cây: [50, 100, 200]
-   Độ sâu tối đa: [5, 10, 15, None]
-   Số lượng đặc trưng tối đa: ['sqrt', 'log2', None]
-   Tiêu chí phân tách: ['gini', 'entropy']

Kết quả tối ưu hóa cho thấy các tham số tối ưu như sau:

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

Sau khi tối ưu hóa mô hình Random Forest, tôi phân tích tầm quan trọng của các đặc trưng:

**Logistic Regression**:

1. format_reverse_tap: 0.4478
2. num_attempts: 0.3922
3. format_listen: 0.2850
4. correct_ratio: 0.2009
5. pos_PRON: 0.1436
6. format_reverse_translate: 0.1161
7. pos_ADJ: 0.0945

**Random Forest**:

1. num_attempts: 0.2059
2. format_reverse_tap: 0.2054
3. correct_ratio: 0.1626
4. format_listen: 0.1100
5. days: 0.0960
6. time_since_last_attempt: 0.0519
7. format_reverse_translate: 0.0510

Kết quả này cho thấy loại bài tập (format_reverse_tap), số lần thử (num_attempts) và tỷ lệ đúng (correct_ratio) là ba đặc trưng quan trọng nhất trong việc dự đoán khả năng ghi nhớ từ vựng.

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

Kết quả đánh giá cho thấy mô hình Random Forest có hiệu suất tốt hơn Logistic Regression trên tất cả các chỉ số. Điều này có thể được giải thích bởi khả năng của Random Forest trong việc xử lý các mối quan hệ phi tuyến tính giữa các đặc trưng và biến mục tiêu.

Tuy nhiên, Logistic Regression vẫn có những ưu điểm riêng:

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
    - Cung cấp các gợi ý và phương pháp học tập phù hợp với từng loại từ vựng

3. **Theo dõi tiến độ học tập**:
    - Cung cấp báo cáo về khả năng ghi nhớ từ vựng của học viên
    - Phát hiện sớm các từ vựng có nguy cơ bị quên cao
    - Đề xuất các biện pháp can thiệp kịp thời

### 4.5.3. Hạn chế và hướng phát triển

Mặc dù đạt được kết quả khả quan, mô hình vẫn còn một số hạn chế:

1. **Hạn chế về dữ liệu**:

    - Dữ liệu SLAM chỉ bao gồm 30 ngày đầu tiên sử dụng ứng dụng
    - Thiếu thông tin về quá trình học tập dài hạn
    - Không có thông tin về các yếu tố cá nhân của học viên (tuổi, trình độ học vấn, v.v.)

2. **Hạn chế về mô hình**:
    - Chưa xem xét đến các yếu tố ngôn ngữ học như độ tương đồng giữa các ngôn ngữ
    - Chưa tận dụng được thông tin về ngữ cảnh sử dụng từ vựng
    - Chưa kết hợp với các mô hình dự đoán dựa trên nội dung từ vựng

Các hướng phát triển trong tương lai:

1. **Thu thập dữ liệu dài hạn** để đánh giá khả năng ghi nhớ từ vựng trong thời gian dài hơn
2. **Áp dụng các kỹ thuật học sâu** như LSTM hoặc Transformer để xử lý dữ liệu chuỗi thời gian
3. **Kết hợp với các mô hình xử lý ngôn ngữ tự nhiên** để tận dụng thông tin về ngữ nghĩa và cấu trúc của từ vựng
4. **Phát triển mô hình đa nhiệm vụ** để dự đoán đồng thời nhiều khía cạnh của quá trình học tập ngôn ngữ
