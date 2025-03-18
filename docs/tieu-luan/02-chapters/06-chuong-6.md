# Chương 6: Ứng dụng thực tế và đề xuất cải tiến trong tương lai

## 6.1. Ứng dụng thực tế của mô hình dự đoán khả năng ghi nhớ từ vựng

Dựa trên kết quả của mô hình Random Forest và Logistic Regression với độ chính xác khoảng 85.8%, tôi đề xuất các ứng dụng thực tế sau đây:

### 6.1.1. Cá nhân hóa lịch trình ôn tập

Mô hình có thể được tích hợp vào các ứng dụng học ngôn ngữ để cá nhân hóa lịch trình ôn tập của học viên:

-   **Tối ưu hóa khoảng thời gian ôn tập**: Dựa trên dự đoán xác suất quên của từng từ vựng, hệ thống có thể điều chỉnh khoảng thời gian giữa các lần ôn tập để tối đa hóa hiệu quả ghi nhớ.

-   **Ưu tiên từ vựng có nguy cơ quên cao**: Hệ thống có thể sắp xếp lại thứ tự ôn tập, đưa các từ vựng có nguy cơ quên cao lên đầu danh sách, giúp học viên tập trung vào những từ vựng khó nhớ.

-   **Thông báo nhắc nhở thông minh**: Gửi thông báo nhắc nhở học viên ôn tập vào thời điểm tối ưu, dựa trên dự đoán của mô hình về thời điểm mà học viên có khả năng bắt đầu quên từ vựng.

### 6.1.2. Tối ưu hóa loại bài tập

Dựa trên kết quả phân tích tầm quan trọng của đặc trưng, tôi thấy rằng loại bài tập (đặc biệt là format_reverse_tap) có ảnh hưởng lớn đến khả năng ghi nhớ từ vựng. Vì vậy, hệ thống có thể:

-   **Điều chỉnh tỷ lệ các loại bài tập**: Tăng tỷ lệ bài tập dạng reverse_tap cho các từ vựng khó nhớ, giúp tăng cường khả năng ghi nhớ.

-   **Cá nhân hóa loại bài tập**: Dựa trên phân tích hiệu quả của từng loại bài tập đối với từng học viên, hệ thống có thể đề xuất loại bài tập phù hợp nhất cho mỗi học viên.

-   **Thiết kế bài tập mới**: Phát triển các loại bài tập mới dựa trên các đặc điểm của bài tập hiệu quả, nhằm tăng cường khả năng ghi nhớ từ vựng.

### 6.1.3. Phân tích tiến độ học tập

Mô hình có thể được sử dụng để phân tích tiến độ học tập của học viên và cung cấp phản hồi chi tiết:

-   **Báo cáo khả năng ghi nhớ**: Cung cấp báo cáo chi tiết về khả năng ghi nhớ từ vựng của học viên, bao gồm các từ vựng đã thuộc, đang học và có nguy cơ quên.

-   **Phân tích điểm mạnh và điểm yếu**: Xác định loại từ vựng mà học viên dễ hoặc khó ghi nhớ (ví dụ: đại từ, tính từ, danh từ), giúp họ tập trung vào các điểm yếu.

-   **Dự đoán thời gian hoàn thành**: Dựa trên tốc độ học và khả năng ghi nhớ hiện tại, hệ thống có thể dự đoán thời gian cần thiết để học viên đạt được mục tiêu học tập.

## 6.2. Đề xuất cải tiến trong tương lai

Dựa trên kết quả nghiên cứu và các hạn chế của mô hình hiện tại, tôi đề xuất các hướng cải tiến sau đây:

### 6.2.1. Cải tiến về dữ liệu

-   **Thu thập dữ liệu dài hạn**: Mở rộng nghiên cứu với dữ liệu học tập dài hạn (6 tháng hoặc 1 năm) để phân tích sự thay đổi khả năng ghi nhớ từ vựng theo thời gian và xây dựng các mô hình dự đoán chính xác hơn.

-   **Đa dạng hóa nguồn dữ liệu**: Kết hợp dữ liệu từ nhiều nền tảng học ngôn ngữ khác nhau để tăng tính tổng quát của mô hình và khám phá các yếu tố ảnh hưởng đến khả năng ghi nhớ trong các ngữ cảnh học tập khác nhau.

-   **Thu thập dữ liệu về đặc điểm học viên**: Bổ sung thông tin về đặc điểm cá nhân của học viên (tuổi, trình độ học vấn, kinh nghiệm học ngôn ngữ) để phân tích ảnh hưởng của các yếu tố này đến khả năng ghi nhớ từ vựng.

### 6.2.2. Cải tiến về mô hình

-   **Sử dụng kỹ thuật học sâu**: Áp dụng các mô hình học sâu như Recurrent Neural Networks (RNN), Long Short-Term Memory (LSTM) hoặc Transformer để phân tích chuỗi dữ liệu hành vi theo thời gian và nắm bắt các mối quan hệ phức tạp giữa các đặc trưng.

-   **Mô hình đa nhiệm vụ**: Phát triển mô hình học đa nhiệm vụ để dự đoán đồng thời nhiều khía cạnh của quá trình học tập ngôn ngữ, như khả năng ghi nhớ từ vựng, thời gian học tập tối ưu và loại bài tập phù hợp.

-   **Học tăng cường**: Áp dụng các kỹ thuật học tăng cường để tối ưu hóa lịch trình ôn tập dựa trên phản hồi của học viên và cải thiện hiệu quả học tập theo thời gian.

### 6.2.3. Cải tiến về đặc trưng

-   **Phân tích ngữ nghĩa**: Bổ sung các đặc trưng về ngữ nghĩa của từ vựng, như mức độ trừu tượng, tần suất xuất hiện trong ngôn ngữ, và mối liên hệ với các từ vựng khác, để phân tích ảnh hưởng của các yếu tố này đến khả năng ghi nhớ.

-   **Đặc trưng ngữ cảnh**: Khai thác thông tin về ngữ cảnh sử dụng từ vựng (ví dụ: từ xuất hiện trong câu, đoạn văn) để đánh giá ảnh hưởng của ngữ cảnh đến khả năng ghi nhớ.

-   **Đặc trưng đa phương tiện**: Phân tích ảnh hưởng của các yếu tố đa phương tiện (hình ảnh, âm thanh) đến khả năng ghi nhớ từ vựng và xây dựng các mô hình dự đoán kết hợp thông tin từ nhiều nguồn.

## 6.3. Kết luận

Nghiên cứu này đã xây dựng và đánh giá các mô hình học máy để dự đoán khả năng ghi nhớ từ vựng tiếng Anh dựa trên dữ liệu hành vi học tập từ Duolingo. Kết quả cho thấy cả hai mô hình Logistic Regression và Random Forest đều đạt độ chính xác tương đương nhau, khoảng 85.8%, với các đặc trưng quan trọng bao gồm loại bài tập, số lần thử và tỷ lệ trả lời đúng.

Mặc dù có một số hạn chế, như độ nhạy thấp và dữ liệu chỉ bao gồm 30 ngày đầu tiên sử dụng ứng dụng, nhưng kết quả nghiên cứu vẫn có giá trị thực tiễn đáng kể. Các mô hình dự đoán có thể được tích hợp vào các ứng dụng học ngôn ngữ để cá nhân hóa lịch trình ôn tập, tối ưu hóa loại bài tập và phân tích tiến độ học tập của học viên.

Toàn bộ mã nguồn của nghiên cứu này được công khai tại [GitHub](https://github.com/limpaulfin/HUB-Fong-VocabRetention-ML/), cho phép các nhà nghiên cứu, giáo viên và nhà phát triển giáo dục ứng dụng kiểm tra, sử dụng lại, và mở rộng các mô hình và phương pháp được trình bày trong tiểu luận này.

Trong tương lai, nghiên cứu có thể được mở rộng theo nhiều hướng, bao gồm thu thập dữ liệu dài hạn, áp dụng các kỹ thuật học sâu và bổ sung các đặc trưng mới để cải thiện hiệu suất dự đoán và tăng cường hiểu biết về quá trình học tập ngôn ngữ. Những cải tiến này sẽ góp phần phát triển các công cụ học tập ngôn ngữ hiệu quả hơn, giúp người học cải thiện khả năng ghi nhớ từ vựng và đạt được các mục tiêu học tập nhanh chóng hơn.

## 6.4. Phân tích sự phát triển của Duolingo từ 2017-2024

Từ năm 2017 đến 2024, Duolingo đã trải qua nhiều thay đổi đáng kể về mô hình kinh doanh, cách tiếp cận học tập và các tính năng gamification. Phần này sẽ phân tích những cải tiến này và tác động tiềm tàng của chúng đến khả năng ghi nhớ từ vựng của người dùng.

### 6.4.1. Các mốc phát triển quan trọng (2017-2024)

**Năm 2017**:

-   Duolingo đạt giá trị 700 triệu USD sau vòng gọi vốn mới
-   Ra mắt khóa học tiếng Hàn để mở rộng thị trường châu Á
-   Số lượng người dùng hoạt động hàng tháng bắt đầu chững lại

**Năm 2018-2019**:

-   Thuê giám đốc tiếp thị (CMO) đầu tiên để tăng cường chiến lược phát triển người dùng
-   Đạt mức định giá 1,5 tỷ USD (tháng 12/2019)
-   Phát triển mô hình Half-Life Regression (HLR) để dự đoán thời gian ghi nhớ từ vựng

**Năm 2020-2021**:

-   Chuyển từ mô hình cộng tác viên tình nguyện sang thuê chuyên gia ngôn ngữ phát triển khóa học
-   IPO trên sàn NASDAQ vào tháng 7/2021
-   Mở rộng tính năng xã hội và cạnh tranh với việc phát triển hệ thống giải đấu (leaderboards)

**Năm 2022**:

-   Thay đổi lớn về giao diện người dùng với việc chuyển từ cấu trúc "cây kỹ năng" sang "lộ trình học tập" tuyến tính
-   Mua lại studio hoạt hình Detroit-based Gunner để tăng cường nội dung trực quan
-   Tăng cường các tính năng gamification

**Năm 2023-2024**:

-   Ra mắt Duolingo Max, một gói đăng ký cao cấp sử dụng công nghệ GPT-4
-   Mở rộng sang các lĩnh vực mới: toán học và âm nhạc
-   Phát triển tính năng Friend Streak, cho phép bạn bè chia sẻ chuỗi học tập
-   Tăng cường các tính năng xã hội và cạnh tranh

### 6.4.2. Phân tích các cải tiến về trải nghiệm học tập

#### Chuyển đổi từ cấu trúc "cây" sang "lộ trình tuyến tính"

Năm 2022, Duolingo đã thực hiện một thay đổi cấu trúc lớn khi chuyển từ mô hình "cây kỹ năng" sang "lộ trình học tập" tuyến tính. Theo CEO Luis von Ahn, mục tiêu của thay đổi này là:

1. **Giảm sự nhầm lẫn**: Cấu trúc cây truyền thống tạo ra sự không chắc chắn cho người dùng về việc nên tiến lên hay quay lại ôn tập kỹ năng cũ.
2. **Cải thiện kết quả học tập**: Lộ trình tuyến tính được xây dựng dựa trên nguyên lý spaced repetition (ôn tập ngắt quãng), giúp người dùng ghi nhớ tốt hơn.

Thay đổi này có những ưu điểm sau:

-   Lộ trình rõ ràng hơn, giúp người học biết chính xác nên làm gì tiếp theo
-   Các đơn vị được tổ chức theo chủ đề logic hơn
-   Tích hợp các câu chuyện (stories) vào lộ trình học tập, tăng cường phương pháp học thụ động
-   Thân thiện hơn với người mới bắt đầu

Tuy nhiên, cũng có một số nhược điểm:

-   Giảm tự do trong việc chọn nội dung ôn tập
-   Khó tiếp cận lại nội dung đã học trước đó
-   Có thể làm giảm động lực của một số người dùng quen với cấu trúc cũ

#### Cải tiến về nội dung học tập

Duolingo cũng đã cải thiện đáng kể về nội dung học tập:

-   Chuyển từ sử dụng cộng tác viên tình nguyện sang thuê chuyên gia ngôn ngữ để phát triển khóa học
-   Áp dụng tiêu chuẩn CEFR (Khung tham chiếu ngôn ngữ chung của châu Âu)
-   Tăng cường nội dung thụ động như câu chuyện (stories) và podcast
-   Bổ sung tài liệu hướng dẫn ngữ pháp rõ ràng hơn (guidebooks)

### 6.4.3. Phân tích các cải tiến về gamification

Trong giai đoạn 2017-2024, Duolingo đã liên tục cải tiến các tính năng gamification để tăng cường sự tương tác và duy trì người dùng:

#### Hệ thống phần thưởng và động lực

-   **Từ Crown (Vương miện) sang Level (Cấp độ)**: Thay đổi từ hệ thống Crown sang Level với các điểm mốc rõ ràng hơn
-   **Legendary Trophy (Cúp huyền thoại)**: Thay thế cho Legendary Level, áp dụng cho toàn bộ đơn vị thay vì kỹ năng cụ thể
-   **Friend Streak (Chuỗi bạn bè)**: Cho phép bạn bè duy trì chuỗi học tập cùng nhau, tăng cường yếu tố cộng đồng

#### Tính năng xã hội và cạnh tranh

-   **Hệ thống giải đấu (Leagues)**: Người dùng được phân vào các giải đấu hàng tuần dựa trên mức độ tương tác, tạo động lực cạnh tranh
-   **Bảng xếp hạng cải tiến**: Ghép người dùng với những người có mức độ tham gia tương tự trong tuần trước để tạo cạnh tranh công bằng
-   **Tính năng thách đấu (Duolingo Clash)**: Giới thiệu năm 2024, cho phép người dùng cạnh tranh trực tiếp

#### Cá nhân hóa và tương tác

-   **Avatar cá nhân**: Từ 2023, người dùng có thể tạo và tùy chỉnh avatar của riêng mình
-   **Mascot tương tác**: Nhân vật Duo (con cú) được phát triển thành một nhân vật biểu tượng, xuất hiện trong thông báo đẩy
-   **Duolingo Score**: Một hệ thống điểm số tổng hợp để theo dõi tiến trình học tập

### 6.4.4. Tác động đến khả năng ghi nhớ từ vựng

Dựa trên các cải tiến từ 2017-2024, tôi có thể xác định những yếu tố có tác động tích cực đến khả năng ghi nhớ từ vựng:

1. **Lộ trình học tập theo nguyên lý spaced repetition**: Việc chuyển sang lộ trình tuyến tính với ôn tập ngắt quãng tích hợp có thể cải thiện đáng kể khả năng ghi nhớ dài hạn.

2. **Tích hợp nội dung thụ động**: Việc đưa câu chuyện (stories) vào lộ trình chính giúp người dùng tiếp xúc với từ vựng trong ngữ cảnh tự nhiên, cải thiện khả năng ghi nhớ.

3. **Tăng cường động lực thông qua gamification**: Các tính năng như chuỗi học tập (streaks), giải đấu (leagues), và hệ thống phần thưởng giúp duy trì động lực học tập trong thời gian dài, điều này cần thiết cho việc ghi nhớ từ vựng.

4. **Cải thiện chất lượng nội dung**: Việc chuyển sang sử dụng chuyên gia ngôn ngữ và tuân thủ tiêu chuẩn CEFR giúp đảm bảo từ vựng được trình bày và dạy một cách hiệu quả hơn.

5. **Chuẩn hóa quá trình học tập**: Các đơn vị chủ đề rõ ràng và tài liệu hướng dẫn giúp người học nắm vững ngữ cảnh và cấu trúc ngôn ngữ, từ đó cải thiện khả năng ghi nhớ.

Những cải tiến này phù hợp với kết quả phân tích về tầm quan trọng của đặc trưng từ mô hình của nghiên cứu này. Ví dụ, việc nhấn mạnh vào các loại bài tập đa dạng (như format_reverse_tap) và tần suất ôn tập (time_since_last_attempt) trong thiết kế lộ trình học tập mới của Duolingo cho thấy công ty đang áp dụng những nguyên tắc tương tự như những gì mô hình của nghiên cứu này đã xác định.

### 6.4.5. Đề xuất cho nghiên cứu trong tương lai

Dựa trên phân tích sự phát triển của Duolingo từ 2017-2024, tôi đề xuất một số hướng nghiên cứu trong tương lai:

1. **So sánh hiệu quả học tập giữa mô hình "cây" và "lộ trình tuyến tính"**: Nghiên cứu đánh giá tác động của việc chuyển đổi cấu trúc đến khả năng ghi nhớ từ vựng.

2. **Phân tích tác động của các tính năng gamification mới**: Đánh giá mức độ ảnh hưởng của các tính năng như Friend Streak, Avatar, và hệ thống giải đấu đến động lực học tập và khả năng ghi nhớ.

3. **Thu thập dữ liệu mới để đào tạo lại mô hình dự đoán**: Cập nhật mô hình với dữ liệu từ phiên bản Duolingo hiện tại để đánh giá sự thay đổi trong các đặc trưng ảnh hưởng đến việc ghi nhớ từ vựng.

4. **Nghiên cứu vai trò của yếu tố xã hội trong việc ghi nhớ từ vựng**: Phân tích mức độ ảnh hưởng của tương tác xã hội và cạnh tranh đến hiệu quả học tập.

Những nghiên cứu này sẽ giúp cập nhật mô hình dự đoán và áp dụng những bài học từ sự phát triển của Duolingo vào các hệ thống học tập ngôn ngữ khác.
