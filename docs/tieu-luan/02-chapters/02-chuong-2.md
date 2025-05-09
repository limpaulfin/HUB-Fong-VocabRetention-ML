# Chương 2: Tổng quan về các thuật toán dự đoán khả năng ghi nhớ từ vựng

## 2.1. Logistic Regression

**Logistic Regression** là một thuật toán học máy đơn giản nhưng mạnh mẽ, thường được sử dụng trong các bài toán phân loại nhị phân. Trong trường hợp dự đoán khả năng ghi nhớ từ vựng, bài toán có thể được định nghĩa là phân loại xem học viên có nhớ từ vựng (kết quả "đúng" hoặc 1) hay không (kết quả "sai" hoặc 0). Thuật toán này đặc biệt phù hợp khi mối quan hệ giữa các đặc trưng đầu vào và kết quả đầu ra có tính chất tuyến tính hoặc gần tuyến tính.

**Cách hoạt động**:
Logistic Regression sử dụng hàm sigmoid để chuyển đổi đầu ra của một hàm tuyến tính thành xác suất trong khoảng từ 0 đến 1. Công thức cơ bản của hàm sigmoid là:

P(đúng) = 1/(1 + e^-(w_0 + w_1·num_attempts + w_2·num_correct + w_3·time_since_last_attempt + w_4·thời gian ôn tập + w_5·tần suất lặp lại))

với i là các trọng số (weights) được học từ dữ liệu và xi là các đặc trưng đầu vào (ví dụ: số lần thử, thời gian giữa các lần thử).

## 2.2. Random Forest

Random Forest là một thuật toán học máy thuộc nhóm ensemble, kết hợp nhiều cây quyết định (decision trees) để cải thiện độ chính xác và giảm nguy cơ overfitting. Không giống Logistic Regression, Random Forest có khả năng xử lý các mối quan hệ phi tuyến tính và tương tác phức tạp giữa các đặc trưng, khiến nó trở thành một lựa chọn mạnh mẽ hơn trong nhiều bài toán thực tế, bao gồm dự đoán khả năng ghi nhớ từ vựng.

**Cách hoạt động**:
Random Forest hoạt động bằng cách:

-   Tạo nhiều tập dữ liệu con (subsets) từ dữ liệu gốc bằng kỹ thuật bootstrap (lấy mẫu ngẫu nhiên có hoàn lại)
-   Xây dựng một cây quyết định cho mỗi tập dữ liệu con, sử dụng một tập hợp ngẫu nhiên các đặc trưng tại mỗi bước phân chia (split)
-   Kết hợp kết quả dự đoán từ tất cả các cây bằng cách lấy **đa số phiếu** (majority vote) trong bài toán phân loại

## 2.3. So sánh Logistic Regression và Random Forest

| Tiêu chí                   | Logistic Regression                           | Random Forest                                 |
| -------------------------- | --------------------------------------------- | --------------------------------------------- |
| **Độ phức tạp**            | Đơn giản, dễ triển khai                       | Phức tạp hơn, cần nhiều tài nguyên            |
| **Khả năng xử lý dữ liệu** | Tốt khi mối quan hệ tuyến tính                | Tốt với dữ liệu phức tạp, phi tuyến tính      |
| **Giải thích kết quả**     | Dễ, cung cấp trọng số cho từng đặc trưng      | Khó, hoạt động như "hộp đen"                  |
| **Hiệu suất**              | Nhanh, phù hợp dữ liệu nhỏ                    | Chậm hơn, nhưng chính xác hơn với dữ liệu lớn |
| **Tương tác đặc trưng**    | Hạn chế, không nắm bắt tốt tương tác phức tạp | Xuất sắc trong việc phát hiện tương tác       |
