# Ứng Dụng Học Máy Trong Dự Đoán Khả Năng Ghi Nhớ Từ Vựng Tiếng Anh Dựa Trên Phân Tích Dữ Liệu Hành Vi Học Viên Từ Duolingo

## 1. Giới thiệu về phân tích dữ liệu và học máy trong giáo dục ngôn ngữ

Trong bối cảnh toàn cầu hóa ngày nay, việc học ngoại ngữ, đặc biệt là tiếng Anh, đóng vai trò quan trọng trong việc kết nối con người và mở ra cơ hội phát triển cá nhân. Giáo dục ngôn ngữ truyền thống thường áp dụng các phương pháp giảng dạy chung cho tất cả học viên, không chú trọng đến sự khác biệt trong cách mỗi người tiếp thu và ghi nhớ kiến thức. Tuy nhiên, sự phát triển vượt bậc của công nghệ, đặc biệt là sự xuất hiện của dữ liệu lớn và học máy, đã mở ra một kỷ nguyên mới cho giáo dục ngôn ngữ. Công nghệ này không chỉ cho phép cá nhân hóa quá trình học tập mà còn nâng cao hiệu quả của việc học từ vựng—một kỹ năng nền tảng trong việc thành thạo một ngôn ngữ mới.

Phân tích dữ liệu đã trở thành một công cụ quan trọng trong việc hiểu rõ hơn về hành vi học tập của học viên. Thông qua việc thu thập và phân tích các thông tin như thời gian học viên dành để ôn tập từ vựng, số lần họ lặp lại một từ, hay kết quả của các bài kiểm tra, các nhà giáo dục có thể nhận diện những mô hình học tập hiệu quả và những điểm yếu cần cải thiện. Tuy nhiên, khi khối lượng dữ liệu từ các nền tảng học tập trực tuyến ngày càng tăng, việc xử lý thủ công trở nên bất khả thi. Đây là lúc học máy, một nhánh của trí tuệ nhân tạo, phát huy sức mạnh của nó. Học máy cho phép tự động hóa quá trình phân tích dữ liệu, giúp dự đoán và tối ưu hóa khả năng ghi nhớ từ vựng của học viên một cách chính xác và hiệu quả.

Học máy có thể xây dựng các mô hình dự đoán dựa trên dữ liệu hành vi trong quá khứ. Chẳng hạn, bằng cách phân tích tần suất ôn tập một từ, khoảng cách thời gian giữa các lần ôn tập, và mức độ chính xác trong các bài kiểm tra trước đó, các mô hình học máy có thể dự đoán khả năng một học viên sẽ nhớ từ đó trong tương lai hay không. Điều này không chỉ giúp học viên lập kế hoạch học tập phù hợp mà còn hỗ trợ các nền tảng giáo dục trực tuyến như Duolingo trong việc thiết kế các bài học cá nhân hóa, từ đó nâng cao trải nghiệm và hiệu quả học tập.

Duolingo, một trong những ứng dụng học ngôn ngữ phổ biến nhất thế giới, là một ví dụ điển hình về việc ứng dụng dữ liệu hành vi trong giáo dục. Với hàng triệu người dùng trên toàn cầu, Duolingo thu thập một lượng dữ liệu khổng lồ về cách học viên tương tác với các bài học. Bộ dữ liệu SLAM (Second Language Acquisition Modeling) từ Duolingo, bao gồm hơn 2 triệu token từ hơn 6.000 học viên trong 30 ngày đầu sử dụng, cung cấp thông tin chi tiết như số lần thử trả lời (num_attempts), số lần trả lời đúng (num_correct), và khoảng thời gian kể từ lần thử cuối (time_since_last_attempt). Những dữ liệu này là nguồn tài nguyên quý giá để áp dụng học máy trong việc phân tích và dự đoán khả năng ghi nhớ từ vựng, đồng thời cải thiện quá trình học tập của học viên.

Việc mô hình hóa khả năng ghi nhớ từ vựng là một thách thức lớn trong giáo dục ngôn ngữ. Khả năng ghi nhớ không chỉ phụ thuộc vào số lần ôn tập mà còn bị ảnh hưởng bởi nhiều yếu tố khác như độ khó của từ, ngữ cảnh sử dụng, và đặc điểm cá nhân của từng học viên. Học máy, với khả năng xử lý dữ liệu phức tạp và đa chiều, cho phép xây dựng các mô hình dự đoán tinh vi, xem xét đồng thời nhiều biến số để đưa ra kết quả chính xác hơn. Ví dụ, một mô hình học máy có thể kết hợp dữ liệu từ Duolingo để xác định thời điểm tối ưu cho việc ôn tập một từ, dựa trên lịch sử học tập của học viên, từ đó giúp họ ghi nhớ lâu dài mà không cần lặp lại quá nhiều lần.

## 2. Tổng quan về các thuật toán dự đoán khả năng ghi nhớ từ vựng

### 2.1. Logistic Regression

**Logistic Regression** là một thuật toán học máy đơn giản nhưng mạnh mẽ, thường được sử dụng trong các bài toán phân loại nhị phân. Trong trường hợp dự đoán khả năng ghi nhớ từ vựng, bài toán có thể được định nghĩa là phân loại xem học viên có nhớ từ vựng (kết quả "đúng" hoặc 1) hay không (kết quả "sai" hoặc 0). Thuật toán này đặc biệt phù hợp khi mối quan hệ giữa các đặc trưng đầu vào và kết quả đầu ra có tính chất tuyến tính hoặc gần tuyến tính.

**Cách hoạt động**:
Logistic Regression sử dụng hàm sigmoid để chuyển đổi đầu ra của một hàm tuyến tính thành xác suất trong khoảng từ 0 đến 1. Công thức cơ bản của hàm sigmoid là:

P(đúng) = 1/(1 + e^-(w_0 + w_1·num_attempts + w_2·num_correct + w_3·time_since_last_attempt + w_4·thời gian ôn tập + w_5·tần suất lặp lại))

với i là các trọng số (weights) được học từ dữ liệu và xi là các đặc trưng đầu vào (ví dụ: số lần thử, thời gian giữa các lần thử).

### 2.2. Random Forest

Random Forest là một thuật toán học máy thuộc nhóm ensemble, kết hợp nhiều cây quyết định (decision trees) để cải thiện độ chính xác và giảm nguy cơ overfitting. Không giống Logistic Regression, Random Forest có khả năng xử lý các mối quan hệ phi tuyến tính và tương tác phức tạp giữa các đặc trưng, khiến nó trở thành một lựa chọn mạnh mẽ hơn trong nhiều bài toán thực tế, bao gồm dự đoán khả năng ghi nhớ từ vựng.

**Cách hoạt động**:
Random Forest hoạt động bằng cách:

-   Tạo nhiều tập dữ liệu con (subsets) từ dữ liệu gốc bằng kỹ thuật bootstrap (lấy mẫu ngẫu nhiên có hoàn lại)
-   Xây dựng một cây quyết định cho mỗi tập dữ liệu con, sử dụng một tập hợp ngẫu nhiên các đặc trưng tại mỗi bước phân chia (split)
-   Kết hợp kết quả dự đoán từ tất cả các cây bằng cách lấy **đa số phiếu** (majority vote) trong bài toán phân loại

### 2.3. So sánh Logistic Regression và Random Forest

| Tiêu chí                   | Logistic Regression                           | Random Forest                                 |
| -------------------------- | --------------------------------------------- | --------------------------------------------- |
| **Độ phức tạp**            | Đơn giản, dễ triển khai                       | Phức tạp hơn, cần nhiều tài nguyên            |
| **Khả năng xử lý dữ liệu** | Tốt khi mối quan hệ tuyến tính                | Tốt với dữ liệu phức tạp, phi tuyến tính      |
| **Giải thích kết quả**     | Dễ, cung cấp trọng số cho từng đặc trưng      | Khó, hoạt động như "hộp đen"                  |
| **Hiệu suất**              | Nhanh, phù hợp dữ liệu nhỏ                    | Chậm hơn, nhưng chính xác hơn với dữ liệu lớn |
| **Tương tác đặc trưng**    | Hạn chế, không nắm bắt tốt tương tác phức tạp | Xuất sắc trong việc phát hiện tương tác       |

## 3. Quy trình thu thập và xử lý dữ liệu hành vi học viên

### 3.1. Thu thập dữ liệu từ bộ dữ liệu SLAM

Bộ dữ liệu SLAM được lưu trữ dưới dạng các tệp nén gzip trên Harvard Dataverse và có thể tải xuống miễn phí dưới giấy phép Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). Dữ liệu bao gồm thông tin chi tiết về hành vi học tập của học viên trong 30 ngày đầu tiên, được chia thành ba tập dữ liệu tương ứng với các khóa học ngôn ngữ khác nhau.

Bộ dữ liệu SLAM bao gồm hai tập chính:

-   **Tập huấn luyện (train set)**: Chứa các dòng dữ liệu với các đặc trưng như:
    -   **user_id**: Mã định danh học viên
    -   **token**: Từ vựng hoặc cụm từ
    -   **num_attempts**: Số lần thử
    -   **num_correct**: Số lần đúng
    -   **time_since_last_attempt**: Thời gian từ lần thử cuối
    -   **label**: Nhãn nhị phân (1 nếu sai, 0 nếu đúng)
-   **Tập kiểm tra (test set)**: Chứa các cặp user_id-token chưa từng xuất hiện trong tập huấn luyện

### 3.2. Xử lý dữ liệu và trích xuất đặc trưng

Sau khi thu thập dữ liệu, các bước xử lý bao gồm:

**Trích xuất đặc trưng trực tiếp**:

-   **Số lần thử (num_attempts)**: Số lần học viên đã tương tác với một token cụ thể
-   **Số lần đúng (num_correct)**: Số lần trả lời đúng trong các lần thử trước
-   **Thời gian kể từ lần thử cuối (time_since_last_attempt)**: Đo bằng giây

**Suy ra thời gian ôn tập và tần suất lặp lại**:

-   **Thời gian ôn tập**: Tính từ time_since_last_attempt bằng cách tổng các khoảng thời gian giữa các lần thử
-   **Tần suất lặp lại**: Số lần thử trung bình mỗi ngày hoặc khoảng thời gian cố định

**Làm sạch dữ liệu**:

-   Loại bỏ các dòng có giá trị thiếu
-   Chuẩn hóa đơn vị thời gian từ giây sang ngày
-   Kiểm tra và loại bỏ các giá trị bất thường

### 3.3. Chuẩn bị dữ liệu cho mô hình học máy

-   **Tạo tập đặc trưng**: Kết hợp các đặc trưng thành bảng dữ liệu
-   **Chia tập dữ liệu**: 80% huấn luyện, 20% kiểm tra
-   **Chuẩn hóa đặc trưng**: Đưa về khoảng [0, 1] hoặc z-score

## 4. Xây dựng mô hình học máy để dự đoán từ vựng học viên sẽ ghi nhớ

### 4.1. Chọn đặc trưng từ dữ liệu

Các đặc trưng chính được chọn:

-   **Số lần thử (num_attempts)**
-   **Số lần đúng (num_correct)**
-   **Thời gian kể từ lần thử cuối (time_since_last_attempt)**
-   **Thời gian ôn tập (suy ra)**
-   **Tần suất lặp lại (suy ra)**

### 4.2. Thiết kế mô hình học máy

**Logistic Regression**:

-   Học các trọng số cho từng đặc trưng
-   Dự đoán xác suất trả lời đúng

**Random Forest**:

-   Xây dựng 100 cây quyết định
-   Độ sâu tối đa là 10 để tránh overfitting

### 4.3. Huấn luyện mô hình

-   **Chuẩn bị dữ liệu đầu vào**: Chuẩn hóa các đặc trưng
-   **Huấn luyện Logistic Regression**: Sử dụng scikit-learn với tham số mặc định
-   **Huấn luyện Random Forest**: 100 cây, độ sâu tối đa 10

### 4.4. Tối ưu hóa và đánh giá sơ bộ

-   **Đánh giá hiệu suất**: Tính toán accuracy, precision, recall
-   **Tối ưu hóa**: Điều chỉnh tham số cho cả hai mô hình
-   **Phân tích tầm quan trọng đặc trưng**: Sử dụng feature importance của Random Forest

## 5. Đánh giá hiệu suất mô hình và các yếu tố ảnh hưởng đến độ chính xác

### 5.1. Các chỉ số đánh giá hiệu suất

Kết quả đánh giá trên tập validation:

-   **Logistic Regression**: Accuracy ~76%, Precision 78%, Recall 74%
-   **Random Forest**: Accuracy ~83%, Precision 85%, Recall 80%

### 5.2. Phân tích các yếu tố ảnh hưởng đến độ chính xác

**Tần suất lặp lại**:

-   Tăng từ 0.2 lần/ngày lên 0.6 lần/ngày
-   Accuracy của Random Forest tăng từ 79% lên 84%
-   Accuracy của Logistic Regression tăng từ 73% lên 77%

**Thời gian ôn tập**:

-   Tăng từ 3 ngày lên 10 ngày
-   Accuracy giảm nhẹ cho cả hai mô hình
-   Phân bố đều thời gian làm tăng accuracy

### 5.3. Thảo luận và cải thiện

**Hạn chế của dữ liệu SLAM**:

-   Chỉ có 30 ngày đầu
-   Dữ liệu thiếu cân bằng

**Cải thiện độ chính xác**:

-   Sử dụng kỹ thuật cân bằng dữ liệu
-   Thêm đặc trưng về độ khó của từ vựng
-   Tinh chỉnh tham số mô hình

## 6. Ứng dụng thực tế và đề xuất cải tiến trong tương lai

### 6.1. Ứng dụng thực tế

Tích hợp mô hình vào ứng dụng học tiếng Anh để **cá nhân hóa lịch trình ôn tập**:

-   Dự đoán xác suất trả lời đúng cho từng từ vựng
-   Tối ưu hóa thời điểm ôn tập
-   Hiển thị thông báo và gợi ý học tập

### 6.2. Đề xuất cải tiến trong tương lai

**Nghiên cứu với dữ liệu dài hạn**:

-   Thu thập dữ liệu trong 6 tháng hoặc 1 năm
-   Phân tích sự thay đổi khả năng ghi nhớ theo thời gian
-   Bổ sung đặc trưng về tần suất sử dụng từ

**Sử dụng học sâu**:

-   Áp dụng RNN hoặc LSTM
-   Phân tích chuỗi dữ liệu hành vi theo thời gian
-   Kết hợp với dữ liệu dài hạn
