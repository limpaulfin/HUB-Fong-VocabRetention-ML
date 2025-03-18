# Tóm tắt

Tiểu luận này nghiên cứu việc ứng dụng học máy trong dự đoán khả năng ghi nhớ từ vựng tiếng Anh của học viên, dựa trên phân tích dữ liệu hành vi từ nền tảng học ngôn ngữ Duolingo. Nghiên cứu tập trung vào việc xây dựng các mô hình học máy như Logistic Regression và Random Forest để dự đoán khả năng ghi nhớ từ vựng, từ đó cá nhân hóa quá trình học tập và nâng cao hiệu quả ghi nhớ từ vựng.

Dữ liệu được sử dụng là bộ dữ liệu SLAM (Second Language Acquisition Modeling) từ Duolingo, bao gồm thông tin về hành vi học tập của hơn 6.000 học viên trong 30 ngày đầu sử dụng ứng dụng. Các đặc trưng chính được sử dụng bao gồm số lần thử, tỷ lệ trả lời đúng, thời gian kể từ lần thử cuối, cùng với loại bài tập và loại từ.

Kết quả nghiên cứu cho thấy cả hai mô hình Random Forest và Logistic Regression đều đạt hiệu suất tương đương với độ chính xác khoảng 85.8%. Các yếu tố ảnh hưởng quan trọng nhất đến khả năng ghi nhớ từ vựng bao gồm loại bài tập (đặc biệt là bài tập reverse_tap), số lần thử và tỷ lệ trả lời đúng. Nghiên cứu cũng đề xuất các cải tiến trong tương lai như sử dụng dữ liệu dài hạn và áp dụng các kỹ thuật học sâu như RNN hoặc LSTM để phân tích chuỗi dữ liệu hành vi theo thời gian.

**Từ khóa**: học máy, dự đoán ghi nhớ từ vựng, Duolingo, SLAM, Logistic Regression, Random Forest

<!--
Đã cập nhật các số liệu thực tế sau khi hoàn thành phân tích dữ liệu:
1. Độ chính xác thực tế của mô hình Random Forest: 85.82%
2. Độ chính xác thực tế của mô hình Logistic Regression: 85.80%
3. Các yếu tố ảnh hưởng chính: format_reverse_tap, num_attempts, correct_ratio
-->
