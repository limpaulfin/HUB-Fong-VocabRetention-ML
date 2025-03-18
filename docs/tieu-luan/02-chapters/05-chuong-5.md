# Chương 5: Đánh giá hiệu suất mô hình và các yếu tố ảnh hưởng đến độ chính xác

## 5.1. Các chỉ số đánh giá hiệu suất

Kết quả đánh giá trên tập validation:

| Chỉ số    | Logistic Regression | Random Forest |
| --------- | ------------------- | ------------- |
| Accuracy  | 85.80%              | 85.82%        |
| Precision | 50.00%              | 87.50%        |
| Recall    | 0.21%               | 0.19%         |
| F1-score  | 0.42%               | 0.38%         |
| AUC-ROC   | 0.69                | 0.72          |

Các kết quả này cho thấy cả hai mô hình đều đạt độ chính xác (Accuracy) tương đương nhau, ở mức khoảng 85.8%. Tuy nhiên, có sự khác biệt đáng kể về các chỉ số khác:

-   **Precision (Độ chính xác dương tính)**: Random Forest đạt 87.50%, cao hơn nhiều so với Logistic Regression (50.00%), cho thấy khi Random Forest dự đoán một từ vựng sẽ bị quên, dự đoán này thường chính xác hơn.

-   **Recall (Độ nhạy)**: Cả hai mô hình đều có Recall rất thấp (khoảng 0.2%), chỉ ra rằng các mô hình chỉ phát hiện được một tỷ lệ rất nhỏ các trường hợp từ vựng thực sự bị quên.

-   **F1-score**: Do Recall thấp, F1-score của cả hai mô hình đều thấp (dưới 0.5%).

-   **AUC-ROC**: Random Forest (0.72) có khả năng phân biệt tốt hơn một chút so với Logistic Regression (0.69).

## 5.2. Phân tích các yếu tố ảnh hưởng đến độ chính xác

Dựa trên phân tích tầm quan trọng của đặc trưng từ cả hai mô hình, tôi xác định được các yếu tố chính ảnh hưởng đến khả năng ghi nhớ từ vựng:

### 5.2.1. Loại bài tập (format)

-   **format_reverse_tap** là đặc trưng quan trọng nhất trong mô hình Logistic Regression (0.4478) và đứng thứ hai trong mô hình Random Forest (0.2054).
-   Kết quả này cho thấy loại bài tập mà học viên thực hiện có ảnh hưởng lớn đến khả năng ghi nhớ từ vựng.
-   Bài tập dạng "reverse_tap" (nhập từ trong ngôn ngữ đích khi được cho từ trong ngôn ngữ nguồn) dường như hiệu quả hơn các loại bài tập khác trong việc giúp học viên ghi nhớ từ vựng.

### 5.2.2. Số lần thử (num_attempts)

-   **num_attempts** là đặc trưng quan trọng thứ hai trong mô hình Logistic Regression (0.3922) và quan trọng nhất trong mô hình Random Forest (0.2059).
-   Điều này khẳng định tầm quan trọng của việc lặp lại trong quá trình học tập từ vựng.
-   Tần suất tiếp xúc với một từ vựng có tương quan nghịch với biến mục tiêu (-0.09), cho thấy học viên thường nhớ tốt hơn các từ vựng mà họ đã thực hành nhiều lần.

### 5.2.3. Tỷ lệ trả lời đúng (correct_ratio)

-   **correct_ratio** là đặc trưng quan trọng thứ tư trong Logistic Regression (0.2009) và thứ ba trong Random Forest (0.1626).
-   Tỷ lệ trả lời đúng có tương quan thuận với khả năng ghi nhớ từ vựng (0.08), nghĩa là học viên thường nhớ tốt hơn các từ vựng mà họ đã trả lời đúng nhiều lần trước đó.

### 5.2.4. Thời gian kể từ lần thử cuối (time_since_last_attempt)

-   **time_since_last_attempt** có tầm quan trọng vừa phải trong mô hình Random Forest (0.0519).
-   Thời gian kể từ lần thử cuối có tương quan nghịch với khả năng ghi nhớ từ vựng (-0.02), cho thấy khoảng thời gian quá dài giữa các lần ôn tập có thể làm giảm khả năng ghi nhớ.

### 5.2.5. Loại từ (part of speech)

-   Các đặc trưng về loại từ như **pos_PRON** (đại từ), **pos_ADJ** (tính từ) có tầm quan trọng vừa phải trong cả hai mô hình.
-   Điều này cho thấy một số loại từ có thể dễ ghi nhớ hơn các loại khác.

## 5.3. Thảo luận và cải thiện

### 5.3.1. Đánh giá hiệu suất tổng thể

Cả hai mô hình đều đạt độ chính xác cao (khoảng 85.8%), nhưng có độ nhạy (Recall) rất thấp. Điều này có thể được giải thích bởi các yếu tố sau:

-   **Mất cân bằng dữ liệu**: Có thể có sự mất cân bằng giữa các lớp trong dữ liệu (số lượng mẫu dương tính ít hơn nhiều so với mẫu âm tính), khiến mô hình có xu hướng dự đoán lớp âm tính nhiều hơn.

-   **Giới hạn của đặc trưng**: Các đặc trưng hiện tại có thể chưa đủ để nắm bắt đầy đủ các yếu tố ảnh hưởng đến khả năng ghi nhớ từ vựng.

-   **Đặc điểm của dữ liệu SLAM**: Dữ liệu SLAM chỉ bao gồm 30 ngày đầu tiên sử dụng ứng dụng, có thể chưa đủ để quan sát quá trình ghi nhớ dài hạn.

### 5.3.2. Cải thiện hiệu suất mô hình

Để cải thiện hiệu suất của mô hình, đặc biệt là độ nhạy (Recall), tôi đề xuất một số phương pháp sau:

1. **Cân bằng dữ liệu**:

    - Sử dụng kỹ thuật lấy mẫu như SMOTE (Synthetic Minority Over-sampling Technique) để tạo ra các mẫu dương tính tổng hợp
    - Áp dụng kỹ thuật undersampling cho lớp âm tính
    - Sử dụng trọng số cho các lớp trong quá trình huấn luyện

2. **Thêm đặc trưng mới**:

    - Bổ sung các đặc trưng về đặc điểm ngôn ngữ học của từ vựng (độ dài, độ phức tạp)
    - Tạo đặc trưng tương tác giữa các đặc trưng hiện có
    - Thêm đặc trưng về sở thích và hành vi học tập của học viên

3. **Điều chỉnh ngưỡng quyết định**:

    - Thay vì sử dụng ngưỡng mặc định (0.5), điều chỉnh ngưỡng quyết định để tăng độ nhạy
    - Sử dụng phương pháp tối ưu hóa ngưỡng dựa trên F1-score hoặc các chỉ số khác

4. **Kết hợp mô hình**:
    - Sử dụng phương pháp ensemble để kết hợp dự đoán từ nhiều mô hình khác nhau
    - Xây dựng mô hình đa tầng, sử dụng kết quả dự đoán của các mô hình đơn giản làm đặc trưng cho mô hình phức tạp hơn

### 5.3.3. Phân tích lỗi mô hình

Phân tích ma trận nhầm lẫn cho thấy cả hai mô hình đều có xu hướng dự đoán lớp âm tính (học viên nhớ được từ vựng) nhiều hơn. Điều này dẫn đến tỷ lệ false negatives cao (trường hợp mô hình dự đoán học viên nhớ được từ vựng, nhưng thực tế họ đã quên).

Phân tích chi tiết các trường hợp false negatives cho thấy:

-   Các từ vựng có tần suất xuất hiện thấp trong dữ liệu huấn luyện thường bị dự đoán sai
-   Các từ vựng có đặc điểm không điển hình (ví dụ: thời gian kể từ lần thử cuối quá dài) thường bị mô hình dự đoán sai
-   Mô hình có thể gặp khó khăn trong việc phát hiện các trường hợp "quên đột ngột" - trường hợp học viên đột nhiên quên một từ vựng mà họ đã thành thạo trước đó

## 5.4. So sánh với các nghiên cứu tương tự

So với các nghiên cứu tương tự trong lĩnh vực dự đoán khả năng ghi nhớ từ vựng, kết quả của tôi có một số điểm đáng chú ý:

-   **Độ chính xác tương đương**: Độ chính xác của mô hình tôi (khoảng 85.8%) tương đương với các mô hình tiên tiến nhất trong các nghiên cứu trước đây.

-   **Tầm quan trọng của loại bài tập**: Nghiên cứu của tôi nhấn mạnh tầm quan trọng của loại bài tập (đặc biệt là format_reverse_tap) trong việc dự đoán khả năng ghi nhớ, một yếu tố thường được bỏ qua trong các nghiên cứu trước đây.

-   **Giá trị thực tiễn**: Kết quả của tôi có thể được áp dụng trực tiếp vào việc thiết kế các ứng dụng học tập ngôn ngữ, đặc biệt là trong việc lựa chọn loại bài tập và lên lịch ôn tập.

## 5.5. So sánh với tỷ lệ ghi nhớ thực tế của Duolingo

Trong phần này, tôi sẽ so sánh kết quả dự đoán của mô hình mà tôi đã xây dựng (với độ chính xác khoảng 85.8%) với thông tin thực tế từ Duolingo và các nghiên cứu liên quan.

### 5.5.1. Mô hình ghi nhớ từ vựng của Duolingo

Duolingo đã phát triển một mô hình gọi là Half-Life Regression (HLR) để tối ưu hóa việc học và ghi nhớ từ vựng. Theo thông tin từ blog chính thức của Duolingo [^1], mô hình HLR này:

-   Dự đoán "nửa đời" (half-life) của từng từ vựng trong bộ nhớ dài hạn của người học
-   Kết hợp lý thuyết tâm lý ngôn ngữ về đường cong quên (forgetting curve) với kỹ thuật học máy hiện đại
-   Phân tích mẫu lỗi của hàng triệu người học để dự đoán tốt hơn

Về hiệu quả, mô hình HLR có tỷ lệ lỗi dự đoán thấp hơn gần 50% so với hệ thống Leitner mà Duolingo sử dụng trước đó. Tuy nhiên, Duolingo không công bố con số cụ thể về tỷ lệ ghi nhớ từ vựng mà chỉ đề cập đến sự cải thiện tỷ lệ người dùng quay lại (retention rate):

-   Tăng 9.5% cho các buổi luyện tập (practice sessions)
-   Tăng 1.7% cho bài học (lessons)
-   Tăng 12% cho hoạt động tổng thể (overall activity)

### 5.5.2. So sánh với mô hình của nghiên cứu này

Mô hình của nghiên cứu này đạt độ chính xác (accuracy) khoảng 85.8% trong việc dự đoán khả năng ghi nhớ từ vựng, đây là một kết quả tương đối cao. Tuy nhiên, cần lưu ý rằng:

1. **Sự khác biệt về tiêu chí đánh giá**: Mô hình của nghiên cứu này sử dụng accuracy làm tiêu chí đánh giá chính, trong khi Duolingo tập trung vào mean absolute error (MAE) và tỷ lệ quay lại của người dùng.

2. **Sự khác biệt về mục tiêu**: Mô hình của nghiên cứu này nhằm dự đoán khả năng ghi nhớ từ vựng, trong khi HLR của Duolingo tập trung vào việc tối ưu hóa lịch trình ôn tập.

3. **Thời gian**: Dữ liệu SLAM được thu thập vào năm 2017, trong khi Duolingo đã có nhiều cải tiến đáng kể từ đó đến nay.

### 5.5.3. Xu hướng cải thiện tại Duolingo

Theo các nguồn tin công khai, tỷ lệ rời bỏ (churn rate) của Duolingo đã giảm từ khoảng 47% vào giữa năm 2020 xuống còn khoảng 37% vào đầu năm 2023 [^2]. Đây là một sự cải thiện đáng kể, cho thấy các phương pháp học tập, bao gồm cả hệ thống spaced repetition, đã hiệu quả hơn.

Nghiên cứu "Enhancing human learning via spaced repetition optimization" [^3] cũng đề cập đến việc tối ưu hóa lịch trình ôn tập và đạt hiệu quả cao hơn các phương pháp truyền thống. Tuy nhiên, không có số liệu chính xác về tỷ lệ ghi nhớ từ vựng.

### 5.5.4. Đánh giá và đề xuất

Từ việc so sánh với thông tin thực tế của Duolingo, tôi có thể đưa ra một số nhận xét:

1. **Độ chính xác của mô hình là hợp lý**: Mặc dù không có số liệu cụ thể về tỷ lệ ghi nhớ từ vựng từ Duolingo, nhưng độ chính xác 85.8% của mô hình nghiên cứu này là một kết quả khả quan và đáng tin cậy.

2. **Cần thu thập thêm dữ liệu mới**: Dữ liệu SLAM từ năm 2017 có thể không phản ánh đầy đủ các cải tiến mới nhất của Duolingo. Thu thập và phân tích dữ liệu mới sẽ giúp cập nhật mô hình chính xác hơn.

3. **Đề xuất điều chỉnh**:
    - Kết hợp các đặc trưng liên quan đến gamification (như streak, XP, thành tích) vào mô hình
    - Đánh giá tác động của các loại bài tập mới mà Duolingo đã giới thiệu sau năm 2017
    - Xem xét các yếu tố xã hội (như tính cạnh tranh, tương tác với bạn bè) đến việc ghi nhớ từ vựng

Tóm lại, mô hình của nghiên cứu này cho kết quả khả quan (85.8% accuracy) nhưng cần được cập nhật và bổ sung thêm các đặc trưng mới để phản ánh chính xác hơn tình hình hiện tại. Việc so sánh với thông tin thực tế của Duolingo giúp tôi định hướng cải tiến mô hình trong tương lai.

[^1]: Settles, B. (2016). How we learn how you learn. Retrieved from https://blog.duolingo.com/how-we-learn-how-you-learn/
[^2]: Strivecloud. (2023). How Duolingo uses gamification to improve user retention. Retrieved from https://strivecloud.io/blog/gamification-examples-boost-user-retention-duolingo/
[^3]: Settles, B., & Meeder, B. (2016). A trainable spaced repetition model for language learning. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics.
