# Chương 3: Quy trình thu thập và xử lý dữ liệu hành vi học viên

## 3.1. Thu thập dữ liệu từ bộ dữ liệu SLAM

Bộ dữ liệu SLAM (Second Language Acquisition Modeling) được lưu trữ dưới dạng các tệp nén gzip trên Harvard Dataverse dưới giấy phép Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). Dữ liệu này bao gồm thông tin chi tiết về hành vi học tập của học viên trong 30 ngày đầu tiên sử dụng ứng dụng Duolingo. Toàn bộ mã nguồn và quy trình xử lý dữ liệu được công khai tại GitHub repository để đảm bảo tính minh bạch và khả năng tái tạo kết quả.

Bộ dữ liệu được chia thành ba tập dữ liệu tương ứng với ba cặp ngôn ngữ khác nhau: data_en_es (tiếng Anh-Tây Ban Nha), data_es_en (tiếng Tây Ban Nha-Anh), và data_fr_en (tiếng Pháp-Anh). Mỗi tập dữ liệu được tổ chức thành ba phần chính: tập huấn luyện (train), tập phát triển (dev), và tập kiểm tra (test).

### 3.1.1. Cấu trúc dữ liệu SLAM

Mỗi dòng trong tập dữ liệu SLAM chứa thông tin về một lần thử của học viên đối với một token (từ vựng hoặc cụm từ) cụ thể. Các trường thông tin chính bao gồm:

-   **user_id**: Mã định danh học viên (được ẩn danh)
-   **token**: Từ vựng hoặc cụm từ mà học viên đang học
-   **format**: Định dạng bài tập (ví dụ: "reverse_translate" - dịch ngược, "listen" - nghe)
-   **days**: Số ngày kể từ khi học viên bắt đầu sử dụng ứng dụng
-   **time**: Thời gian (tính bằng giây) kể từ khi học viên bắt đầu sử dụng ứng dụng
-   **num_attempts**: Số lần học viên đã thử token này trước đó
-   **num_correct**: Số lần học viên đã trả lời đúng token này trước đó
-   **time_since_last_attempt**: Thời gian (tính bằng giây) kể từ lần cuối học viên thử token này
-   **label**: Nhãn nhị phân (1 nếu học viên trả lời sai, 0 nếu trả lời đúng)

### 3.1.2. Đặc điểm của bộ dữ liệu

Bộ dữ liệu bao gồm dữ liệu của hơn 6.000 học viên với hơn 2 triệu token, được thu thập trong 30 ngày đầu tiên sử dụng ứng dụng. Tập huấn luyện và tập phát triển chứa dữ liệu của cùng một nhóm học viên, trong khi tập kiểm tra chứa dữ liệu của các học viên khác để đánh giá khả năng tổng quát hóa của mô hình. Trong nghiên cứu này, tôi tập trung vào dữ liệu của học viên nói tiếng Tây Ban Nha và Pháp học tiếng Anh (es_en, fr_en).

## 3.2. Xử lý dữ liệu và trích xuất đặc trưng

### 3.2.1. Trích xuất đặc trưng trực tiếp

Các đặc trưng trực tiếp được trích xuất từ bộ dữ liệu SLAM bao gồm:

-   **Số lần thử (num_attempts)**: Số lần học viên đã tương tác với một token cụ thể
-   **Số lần đúng (num_correct)**: Số lần trả lời đúng trong các lần thử trước
-   **Thời gian kể từ lần thử cuối (time_since_last_attempt)**: Đo bằng giây
-   **Tỷ lệ đúng (correct_ratio)**: Tỷ lệ giữa num_correct và num_attempts
-   **Thời gian sử dụng ứng dụng (days)**: Số ngày kể từ khi học viên bắt đầu sử dụng ứng dụng

### 3.2.2. Suy ra thời gian ôn tập và tần suất lặp lại

Từ các đặc trưng trực tiếp, tôi suy ra các đặc trưng bổ sung:

-   **Thời gian ôn tập (review_time)**: Tính từ time_since_last_attempt bằng cách tổng các khoảng thời gian giữa các lần thử
-   **Tần suất lặp lại (repetition_frequency)**: Số lần thử trung bình mỗi ngày
-   **Khoảng cách ôn tập trung bình (average_review_interval)**: Thời gian trung bình giữa các lần ôn tập
-   **Độ khó của token (token_difficulty)**: Tỷ lệ học viên trả lời sai token này trong toàn bộ dữ liệu

### 3.2.3. Làm sạch dữ liệu

Quá trình làm sạch dữ liệu bao gồm loại bỏ các dòng có giá trị thiếu, chuẩn hóa đơn vị thời gian (chuyển đổi từ giây sang ngày), kiểm tra và loại bỏ các giá trị bất thường sử dụng phương pháp IQR (Interquartile Range), và xử lý dữ liệu không cân bằng để đảm bảo số lượng mẫu của các lớp tương đối đồng đều.

## 3.3. Chuẩn bị dữ liệu cho mô hình học máy

### 3.3.1. Tạo tập đặc trưng

Sau khi trích xuất và làm sạch dữ liệu, tôi kết hợp các đặc trưng thành một bảng dữ liệu hoàn chỉnh. Mỗi dòng đại diện cho một lần thử của học viên đối với một token cụ thể, với các cột tương ứng với các đặc trưng đã trích xuất và suy ra.

### 3.3.2. Chia tập dữ liệu

Dữ liệu được chia thành tập huấn luyện (80%) và tập kiểm tra (20%) theo phương pháp phân tầng (stratified sampling) để đảm bảo phân phối của biến mục tiêu trong các tập con tương tự như trong tập dữ liệu gốc.

### 3.3.3. Chuẩn hóa đặc trưng

Các đặc trưng số được chuẩn hóa để đưa về cùng một thang đo, giúp cải thiện hiệu suất của mô hình học máy. Hai phương pháp chuẩn hóa được sử dụng là Min-Max Scaling (đưa các giá trị về khoảng [0, 1]) và Z-score Normalization (chuẩn hóa các giá trị để có trung bình bằng 0 và độ lệch chuẩn bằng 1). Việc lựa chọn phương pháp chuẩn hóa phụ thuộc vào đặc điểm của từng đặc trưng và yêu cầu của thuật toán học máy.
