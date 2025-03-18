# Góp ý từ anh Thịnh - Phân tích và hướng phát triển tiểu luận

## 1. So sánh với tỷ lệ ghi nhớ thực tế

> [18/03/2025 09:32:25] Thịnh: kết quả của 2 mô hình cho ra trung bình khoảng 79% retention, thế còn thực tế của doulingo tự công bố là bn %
>
> [18/03/2025 09:33:05] Thịnh: Hoặc khảo sát người dùng hoặc kết quả từ nguồn khác cho ra bn %

### Phân tích và giải thích:

Ý chính của anh Thịnh là cần so sánh kết quả dự đoán của mô hình (hiện tại là 85.8% accuracy) với các số liệu thực tế từ:

-   Số liệu chính thức mà Duolingo công bố về tỷ lệ ghi nhớ từ vựng
-   Kết quả từ các nghiên cứu độc lập hoặc khảo sát người dùng

Việc so sánh này sẽ giúp:

1. Đánh giá mức độ chính xác của mô hình so với thực tế
2. Hiểu rõ hơn về khoảng cách giữa dự đoán và thực tế
3. Điều chỉnh mô hình để phản ánh chính xác hơn tình hình thực tế

**Hành động cần thực hiện:**

-   Tìm kiếm thông tin chính thức từ Duolingo về tỷ lệ ghi nhớ từ vựng
-   Tìm kiếm các nghiên cứu học thuật đánh giá hiệu quả của Duolingo
-   Thêm phần so sánh này vào mục 5.5 của Chương 5

## 2. Hướng phát triển sâu hơn

> [18/03/2025 09:44:14] Thịnh: Nếu sâu nữa sẽ có những hướng như sau:
>
> 1. Doulingo đã có những cải tiến nhiều kể từ 2017, là thời điểm data này đc công bố, liệu những cải tiến về gamification và cách tương tác này có tăng đc % nào retention ko?
> 2. Xét riêng hệ thống lms của mình:
>    2.1. đã có cơ chế thu lượm những data này ở back end chưa?
>    2.2. thu lượm xong dùng mô hình ML này sẽ trả ra kết quả nào đó, giả sử 50%, thì có thật sự đúng hay ko? Vì cơ chế data set 2 bên có thể khác nhau, có phải cấu hình lại ML để chạy cho 2 data sét khác nhau cho chuẩn xác ko?
>    2.3. với kq ấy thì có đưa ra đc các cách khác dự báo để tăng % retention ko? Và cái này chính là kết quả đáng tiền nhất của tiểu luận này. Không phải mất công A/B test mà mình biết chắc ML đã dự đoán đc thì mạnh dạn cải tiến vì biết rõ Noa mang lại kq ntn

### 2.1. Phân tích sự thay đổi từ 2017 đến nay

#### Giải thích chi tiết:

Bộ dữ liệu SLAM được công bố vào năm 2017. Kể từ đó, Duolingo đã có nhiều cải tiến quan trọng về:

-   Giao diện người dùng
-   Hệ thống gamification (điểm thưởng, thành tích, liên đấu)
-   Cơ chế tương tác và các loại bài tập
-   Thuật toán cá nhân hóa lộ trình học tập

Câu hỏi quan trọng là: **Những cải tiến này đã cải thiện tỷ lệ ghi nhớ từ vựng được bao nhiêu phần trăm?**

Để trả lời câu hỏi này, cần:

1. Nghiên cứu và liệt kê các cải tiến chính của Duolingo từ 2017-2024
2. Phân tích tác động tiềm năng của từng cải tiến đến khả năng ghi nhớ từ vựng
3. Tìm kiếm số liệu về tỷ lệ ghi nhớ từ vựng của Duolingo qua các năm (nếu có)
4. Đề xuất nghiên cứu mới với dữ liệu hiện tại để so sánh với kết quả từ dữ liệu 2017

**Hành động cần thực hiện:**

-   Thêm mục "6.4. Phân tích sự phát triển của Duolingo từ 2017-2024" vào Chương 6
-   Tổng hợp và phân tích các cải tiến chính của Duolingo trong giai đoạn này

### 2.2. Ứng dụng vào hệ thống LMS riêng

#### 2.2.1. Thu thập dữ liệu

Trước khi áp dụng mô hình học máy, cần đánh giá hệ thống LMS hiện tại xem:

-   Đã có cơ chế thu thập dữ liệu hành vi người dùng chưa?
-   Những dữ liệu nào đã được thu thập?
-   Dữ liệu có tương tự với bộ dữ liệu SLAM không?

Các dữ liệu cần thu thập để áp dụng mô hình tương tự như SLAM:

-   Số lần thử (num_attempts)
-   Tỷ lệ trả lời đúng (correct_ratio)
-   Thời gian kể từ lần thử cuối (time_since_last_attempt)
-   Loại bài tập (format)
-   Loại từ (part of speech)

Nếu hệ thống chưa thu thập các dữ liệu này, cần xây dựng quy trình thu thập dữ liệu phù hợp.

#### 2.2.2. Hiệu chỉnh và đánh giá mô hình

Sau khi thu thập dữ liệu, cần:

-   Hiệu chỉnh mô hình để phù hợp với cấu trúc dữ liệu của hệ thống LMS
-   Đánh giá mô hình trên dữ liệu mới
-   So sánh kết quả với mô hình dự đoán trên dữ liệu SLAM

Anh Thịnh đã nêu một điểm quan trọng: "thu lượm xong dùng mô hình ML này sẽ trả ra kết quả nào đó, giả sử 50%, thì có thật sự đúng hay ko?"

Để xác định độ chính xác của mô hình trên dữ liệu mới, cần:

1. Thu thập dữ liệu thực tế về khả năng ghi nhớ từ vựng từ người dùng
2. So sánh dự đoán của mô hình với kết quả thực tế
3. Hiệu chỉnh mô hình nếu có sự chênh lệch lớn

#### 2.2.3. Ứng dụng kết quả dự đoán

Đây là phần "đáng tiền nhất" như anh Thịnh đã nhấn mạnh. Khi có mô hình dự đoán chính xác, có thể:

-   **Cải tiến loại bài tập:** Tăng cường các loại bài tập có tác động tích cực đến khả năng ghi nhớ (như format_reverse_tap)
-   **Tối ưu hóa lịch trình ôn tập:** Điều chỉnh thời gian giữa các lần ôn tập dựa trên dự đoán
-   **Cá nhân hóa trải nghiệm:** Điều chỉnh lộ trình học tập cho từng cá nhân

Việc có một mô hình dự đoán chính xác giúp:

-   Tiết kiệm thời gian và chi phí cho A/B testing
-   Tự tin hơn khi triển khai các cải tiến
-   Dự đoán được tác động của các thay đổi trước khi thực hiện

## 3. Giá trị kinh doanh và xây dựng thương hiệu

> [18/03/2025 09:45:51] Thịnh: Làm đc những cái này mà số liệu chứng minh đc thì đóng góp của e sẽ rất lớn, chỉ riêng đi tư vấn cho các tập đoàn về cải tiến dựa trên đề xuất của ML thì e đã mở ra 1 nhánh kiếm tiền và build thương hiệu mình dựa trên kq đó r

### Phân tích và giải thích:

Anh Thịnh chỉ ra rằng nghiên cứu này không chỉ có giá trị học thuật mà còn có tiềm năng thương mại lớn.

Các hướng phát triển thành dịch vụ tư vấn:

1. **Đánh giá hệ thống học tập hiện tại:**

    - Phân tích dữ liệu hành vi học tập
    - Xác định điểm mạnh và điểm yếu của hệ thống
    - Dự đoán tỷ lệ ghi nhớ từ vựng hiện tại

2. **Đề xuất cải tiến dựa trên mô hình ML:**

    - Tối ưu hóa loại bài tập
    - Cải thiện lịch trình ôn tập
    - Cá nhân hóa trải nghiệm học tập

3. **Đánh giá tác động của cải tiến:**
    - Thiết lập các chỉ số đo lường hiệu quả
    - So sánh kết quả trước và sau khi cải tiến
    - Tính toán ROI (Return on Investment) của các cải tiến

Việc có số liệu chứng minh hiệu quả của các cải tiến sẽ:

-   Tăng tính thuyết phục khi làm việc với khách hàng
-   Xây dựng uy tín và thương hiệu cá nhân trong lĩnh vực EdTech
-   Tạo lợi thế cạnh tranh so với các dịch vụ tư vấn thông thường

**Hành động cần thực hiện:**

-   Thêm mục "6.5. Hướng phát triển thành dịch vụ tư vấn" vào Chương 6
-   Phác thảo mô hình kinh doanh tiềm năng dựa trên kết quả nghiên cứu

## 4. Đề xuất bổ sung vào tiểu luận

Dựa trên các góp ý của anh Thịnh, cần bổ sung các nội dung sau vào tiểu luận:

### Chương 5:

-   Thêm mục "5.5. So sánh với tỷ lệ ghi nhớ thực tế của Duolingo"

### Chương 6:

-   Mở rộng mục "6.1. Ứng dụng thực tế" với chi tiết về triển khai trong hệ thống LMS
-   Thêm mục "6.4. Phân tích sự phát triển của Duolingo từ 2017-2024"
-   Thêm mục "6.5. Hướng phát triển thành dịch vụ tư vấn"

Những nội dung bổ sung này sẽ giúp tiểu luận không chỉ mang tính học thuật mà còn có giá trị ứng dụng thực tế cao, đặc biệt trong môi trường kinh doanh và phát triển sản phẩm EdTech.
