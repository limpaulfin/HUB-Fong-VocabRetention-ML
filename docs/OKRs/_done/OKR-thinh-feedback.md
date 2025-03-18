# OKR-thinh-feedback - Các tác vụ theo góp ý của anh Thịnh

Dựa trên góp ý của anh Thịnh (xem file `docs/raw-materials/gop-y-anh-thinh.md`), chúng ta cần thực hiện các tác vụ sau đây để bổ sung thông tin cho tiểu luận.

## Mục tiêu chính (Objectives)

1. **Bổ sung thông tin so sánh với tỷ lệ ghi nhớ thực tế của Duolingo**
2. **Phân tích sự phát triển của Duolingo từ 2017 đến nay**
3. **Nêu yêu cầu và đề xuất áp dụng mô hình vào hệ thống LMS riêng**
4. **Xây dựng định hướng phát triển dịch vụ tư vấn từ kết quả nghiên cứu**

## Chi tiết kế hoạch thực hiện (Key Results)

### 1. Bổ sung thông tin so sánh với tỷ lệ ghi nhớ thực tế của Duolingo

-   [x] **1.1. Tìm kiếm thông tin từ nguồn chính thức của Duolingo**

    -   [x] Nghiên cứu các bài blog, white paper của Duolingo
    -   [x] Tìm kiếm thông cáo báo chí và báo cáo hàng năm của Duolingo
    -   [x] Khảo sát thông tin từ trang Duolingo Research

    **Kết quả tìm kiếm:**

    -   Duolingo sử dụng mô hình Half-Life Regression (HLR) để dự đoán thời gian ghi nhớ từ vựng
    -   Mô hình HLR giúp giảm tỷ lệ lỗi dự đoán gần 50% so với phương pháp Leitner cũ
    -   Ứng dụng HLR đã cải thiện tỷ lệ người dùng quay lại: tăng 9.5% cho buổi luyện tập, 1.7% cho bài học, và 12% cho hoạt động tổng thể
    -   Duolingo không công bố con số cụ thể về tỷ lệ ghi nhớ từ vựng, nhưng dữ liệu về churn rate đã giảm từ khoảng 47% (2020) xuống 37% (2023)
    -   Nghiên cứu "Enhancing human learning via spaced repetition optimization" đề cập đến việc tối ưu hóa lịch trình ôn tập và đạt hiệu quả cao hơn các phương pháp truyền thống
    -   Có bằng chứng về việc áp dụng spaced repetition đã cải thiện ghi nhớ dài hạn, nhưng không có số liệu chính xác về tỷ lệ ghi nhớ từ vựng

-   [x] **1.2. Tìm kiếm nghiên cứu học thuật về hiệu quả của Duolingo**

    -   [x] Tìm kiếm bài báo khoa học đánh giá hiệu quả học tập trên Duolingo
    -   [x] Tìm các nghiên cứu so sánh Duolingo với các phương pháp học truyền thống
    -   [x] Tổng hợp các số liệu về tỷ lệ ghi nhớ từ vựng từ các nguồn này

    **Kết quả tìm kiếm:**

    -   Đã tìm được nghiên cứu của González-Fernández (2023) về hiệu quả của Duolingo so với phương pháp dạy học truyền thống
    -   Đã tìm được nghiên cứu của Rodríguez-Fuentes & Swatek (2023) về so sánh giữa học trong lớp và học qua ứng dụng Duolingo
    -   Đã tìm được nghiên cứu tổng hợp của Shortt et al. (2023) về gamification trong học ngôn ngữ qua Duolingo
    -   Các nghiên cứu cho thấy hiệu quả học tập tương đương hoặc cao hơn so với phương pháp truyền thống

-   [x] **1.3. Thêm mục 5.5 vào Chương 5 của tiểu luận**

    -   [x] Tổng hợp và so sánh kết quả mô hình (85.8%) với số liệu thực tế
    -   [x] Phân tích nguyên nhân chênh lệch (nếu có)
    -   [x] Đề xuất điều chỉnh để mô hình phản ánh chính xác hơn tình hình thực tế

    **Kết quả:**

    -   Đã tạo mục 5.5 trong file `docs/tieu-luan/02-chapters/05-chuong-5.md`
    -   Đã so sánh kết quả mô hình với mô hình Half-Life Regression (HLR) của Duolingo
    -   Đã phân tích sự khác biệt về tiêu chí đánh giá, mục tiêu và thời gian
    -   Đã đề xuất các điều chỉnh như bổ sung đặc trưng gamification, đánh giá loại bài tập mới

### 2. Phân tích sự phát triển của Duolingo từ 2017 đến nay

-   [x] **2.1. Nghiên cứu các thay đổi và cải tiến của Duolingo từ 2017-2024**

    -   [x] Tìm kiếm thông tin về các cập nhật chính của ứng dụng Duolingo
    -   [x] Nghiên cứu các thay đổi về giao diện và trải nghiệm người dùng
    -   [x] Tìm hiểu về các cải tiến trong hệ thống gamification
    -   [x] Khảo sát sự phát triển của các loại bài tập và phương pháp học

    **Kết quả:**

    -   Đã tìm kiếm và tổng hợp thông tin về các thay đổi chính của Duolingo từ 2017-2024
    -   Đã xác định các mốc phát triển quan trọng: đạt giá trị 700 triệu USD (2017), IPO (2021), thay đổi lộ trình học tập (2022), v.v.
    -   Đã nghiên cứu sự chuyển đổi từ mô hình "cây kỹ năng" sang "lộ trình tuyến tính" năm 2022
    -   Đã tìm hiểu về các cải tiến gamification: hệ thống giải đấu, chuỗi học tập, avatar cá nhân, v.v.

-   [x] **2.2. Phân tích tác động tiềm năng của các cải tiến đến khả năng ghi nhớ từ vựng**

    -   [x] Đánh giá tác động của từng loại cải tiến
    -   [x] Liên hệ với kết quả phân tích tầm quan trọng của đặc trưng từ mô hình
    -   [x] Đề xuất các cải tiến có tiềm năng cải thiện khả năng ghi nhớ nhiều nhất

    **Kết quả:**

    -   Đã phân tích tác động của lộ trình học tập tuyến tính dựa trên spaced repetition đến khả năng ghi nhớ
    -   Đã đánh giá ảnh hưởng của cải tiến về nội dung học tập (chuyên gia ngôn ngữ, tiêu chuẩn CEFR)
    -   Đã phân tích tác động của gamification (hệ thống phần thưởng, tính năng xã hội) đến động lực học tập
    -   Đã liên hệ với kết quả phân tích từ mô hình về tầm quan trọng của đặc trưng format_reverse_tap và time_since_last_attempt

-   [x] **2.3. Thêm mục 6.4 vào Chương 6 của tiểu luận**

    -   [x] Tổng hợp và trình bày các cải tiến quan trọng của Duolingo
    -   [x] Phân tích tác động đến khả năng ghi nhớ từ vựng
    -   [x] Đề xuất nghiên cứu so sánh dữ liệu 2017 với dữ liệu hiện tại

    **Kết quả:**

    -   Đã tạo mục 6.4 "Phân tích sự phát triển của Duolingo từ 2017-2024" trong file `docs/tieu-luan/02-chapters/06-chuong-6.md`
    -   Đã phân tích các mốc phát triển quan trọng từ 2017-2024 và các cải tiến về trải nghiệm học tập
    -   Đã phân tích chi tiết việc chuyển từ cấu trúc "cây" sang "lộ trình tuyến tính" và tác động của nó
    -   Đã phân tích các cải tiến về gamification (phần thưởng, tính năng xã hội, cá nhân hóa)
    -   Đã đánh giá tác động của các cải tiến đến khả năng ghi nhớ từ vựng
    -   Đã đề xuất các hướng nghiên cứu trong tương lai, bao gồm so sánh hiệu quả của các mô hình khác nhau

### 3. Nêu yêu cầu và đề xuất áp dụng mô hình vào hệ thống LMS riêng

-   [ ] **3.1. Mở rộng mục 6.1 trong Chương 6 về triển khai trong hệ thống LMS**

    -   [ ] Xác định các yêu cầu về thu thập dữ liệu hành vi người dùng
    -   [ ] Mô tả quy trình hiệu chỉnh mô hình cho dữ liệu mới
    -   [ ] Đề xuất phương pháp đánh giá hiệu quả của mô hình trên dữ liệu mới

-   [ ] **3.2. Nêu chi tiết quy trình thu thập dữ liệu cần thiết**

    -   [ ] Liệt kê các loại dữ liệu cần thu thập tương tự như SLAM
    -   [ ] Đề xuất phương pháp tổ chức và lưu trữ dữ liệu
    -   [ ] Xây dựng framework thu thập dữ liệu hành vi người dùng

-   [ ] **3.3. Đề xuất mẫu thiết kế API để tích hợp mô hình vào hệ thống LMS**
    -   [ ] Thiết kế mẫu API cho việc thu thập dữ liệu
    -   [ ] Thiết kế mẫu API cho việc dự đoán khả năng ghi nhớ
    -   [ ] Đề xuất cách tích hợp kết quả dự đoán vào quy trình học tập

### 4. Xây dựng định hướng phát triển dịch vụ tư vấn từ kết quả nghiên cứu

-   [ ] **4.1. Thêm mục 6.5 vào Chương 6 của tiểu luận**

    -   [ ] Mô tả cách thức chuyển đổi kết quả nghiên cứu thành dịch vụ tư vấn
    -   [ ] Nêu rõ giá trị kinh doanh của dịch vụ tư vấn
    -   [ ] Đề xuất các bước xây dựng thương hiệu dựa trên kết quả nghiên cứu

-   [ ] **4.2. Phác thảo mô hình kinh doanh tiềm năng**

    -   [ ] Xác định các nhóm khách hàng tiềm năng
    -   [ ] Mô tả các gói dịch vụ tư vấn có thể phát triển
    -   [ ] Đề xuất chiến lược marketing và phát triển khách hàng

-   [ ] **4.3. Xây dựng kế hoạch đánh giá hiệu quả của các cải tiến**
    -   [ ] Thiết lập các chỉ số đo lường hiệu quả (KPI)
    -   [ ] Đề xuất phương pháp đánh giá tác động của các cải tiến
    -   [ ] Xây dựng framework tính toán ROI cho các cải tiến đề xuất

## Nguồn thông tin đáng tin cậy cần tham khảo

### Nguồn chính thức từ Duolingo

-   [Duolingo Blog](https://blog.duolingo.com/)
-   [Duolingo Research](https://research.duolingo.com/)
-   [Duolingo Efficacy Research](https://research.duolingo.com/papers/settles.acl16.pdf)
-   [Duolingo Annual Reports](https://investors.duolingo.com/)

### Nghiên cứu học thuật

-   Settles, B., & Meeder, B. (2016). A trainable spaced repetition model for language learning. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics.
-   Settles, B., Brust, C., Gustafson, E., Hagiwara, M., & Madnani, N. (2018). Second Language Acquisition Modeling. In Proceedings of the NAACL-HLT Workshop on Innovative Use of NLP for Building Educational Applications (BEA).
-   Ye, F. (2014). Validity, reliability, and concordance of the Duolingo English Test. Retrieved from https://s3.amazonaws.com/duolingo-papers/other/ye.testcenter14.pdf

### Các báo cáo và đánh giá độc lập

-   [Common Sense Education's Review of Duolingo](https://www.commonsense.org/education/website/duolingo)
-   [PCMag's Review of Duolingo](https://www.pcmag.com/reviews/duolingo)
-   [Educational App Store's Review of Duolingo](https://www.educationalappstore.com/app/duolingo-learn-languages-for-free)

### Diễn đàn người dùng

-   [Duolingo Forum](https://forum.duolingo.com/)
-   [Reddit r/duolingo](https://www.reddit.com/r/duolingo/)

## Lưu ý quan trọng

-   [x] **Cập nhật tài liệu tham khảo cho tiểu luận với các nguồn mới về Duolingo và spaced repetition**

    -   Đã bổ sung 19 tài liệu tham khảo mới vào file `docs/tieu-luan/03-back-matter/01-references.md`
    -   Đã bổ sung 19 tài liệu tham khảo mới kèm URL vào file `docs/tieu-luan/03-back-matter/01-references-url.md`
    -   Các tài liệu tập trung vào spaced repetition, gamification và sự phát triển của Duolingo từ 2017-2024

-   **Chúng ta không thay đổi mô hình đã xây dựng**, chỉ tập trung vào việc bổ sung thông tin so sánh, khảo sát thêm và thêm định hướng cho tương lai.
-   Khi tìm kiếm thông tin, cần **ưu tiên các nguồn tin cậy** như:
    -   Bài viết chính thức từ Duolingo
    -   Các nghiên cứu được công bố trên tạp chí khoa học uy tín
    -   Các báo cáo từ các tổ chức giáo dục có uy tín
-   Khi đề xuất các ứng dụng và phát triển, cần **dựa trên kết quả nghiên cứu thực tế** đã có.
-   Các đề xuất cần **khả thi và có giá trị thực tiễn**, có thể triển khai được trong môi trường kinh doanh thực tế.

## Thời gian dự kiến hoàn thành

-   Tổng thời gian: 2 tuần
-   Mục tiêu 1: 3 ngày ✅ (Hoàn thành)
-   Mục tiêu 2: 4 ngày ✅ (Hoàn thành)
-   Mục tiêu 3: 3 ngày
-   Mục tiêu 4: 4 ngày

## Người phụ trách

-   Lâm Thanh Phong (Học viên thực hiện)
-   TS. Nguyễn Hoài Đức (Giảng viên hướng dẫn)
