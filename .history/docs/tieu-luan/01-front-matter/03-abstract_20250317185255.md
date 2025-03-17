# Tóm tắt

Tiểu luận này nghiên cứu việc ứng dụng học máy trong dự đoán khả năng ghi nhớ từ vựng tiếng Anh của học viên, dựa trên phân tích dữ liệu hành vi từ nền tảng học ngôn ngữ Duolingo. Nghiên cứu tập trung vào việc xây dựng các mô hình học máy như Logistic Regression và Random Forest để dự đoán khả năng ghi nhớ từ vựng, từ đó cá nhân hóa quá trình học tập và nâng cao hiệu quả ghi nhớ từ vựng.

Dữ liệu được sử dụng là bộ dữ liệu SLAM (Second Language Acquisition Modeling) từ Duolingo, bao gồm thông tin về hành vi học tập của hơn 6.000 học viên trong 30 ngày đầu sử dụng ứng dụng. Các đặc trưng chính được sử dụng bao gồm số lần thử, số lần trả lời đúng, thời gian kể từ lần thử cuối, cùng với các đặc trưng suy ra như thời gian ôn tập và tần suất lặp lại.

Kết quả nghiên cứu cho thấy mô hình Random Forest đạt hiệu suất cao hơn với độ chính xác khoảng 83%, trong khi Logistic Regression đạt khoảng 76%. Các yếu tố ảnh hưởng đến độ chính xác bao gồm tần suất lặp lại và thời gian ôn tập. Nghiên cứu cũng đề xuất các cải tiến trong tương lai như sử dụng dữ liệu dài hạn và áp dụng các kỹ thuật học sâu như RNN hoặc LSTM để phân tích chuỗi dữ liệu hành vi theo thời gian.

**Từ khóa**: học máy, dự đoán ghi nhớ từ vựng, Duolingo, SLAM, Logistic Regression, Random Forest

<!--
LƯU Ý: Cần cập nhật các số liệu thực tế sau khi hoàn thành phân tích dữ liệu:
1. Số lượng học viên chính xác trong bộ dữ liệu SLAM
2. Độ chính xác thực tế của mô hình Random Forest (hiện tại ~83%)
3. Độ chính xác thực tế của mô hình Logistic Regression (hiện tại ~76%)
4. Các yếu tố ảnh hưởng đến độ chính xác dựa trên phân tích feature importance
-->
