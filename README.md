# VocabRetention-ML

Dự án nghiên cứu và phát triển mô hình học máy để dự đoán khả năng ghi nhớ từ vựng tiếng Anh dựa trên dữ liệu hành vi học tập từ Duolingo.

**GitHub Repository:** [https://github.com/limpaulfin/HUB-Fong-VocabRetention-ML/](https://github.com/limpaulfin/HUB-Fong-VocabRetention-ML/)

## Thông tin tác giả

-   **Học viên thực hiện:** Lâm Thanh Phong
-   **Mã số học viên:** 020201240024
-   **Lớp:** HTTTQL01_A1 - đợt 2
-   **Ngành:** Hệ thống thông tin quản lý
-   **Chuyên ngành:** Kinh doanh và trí tuệ nhân tạo
-   **Giảng viên hướng dẫn:** TS. Nguyễn Hoài Đức
-   **Cơ sở đào tạo:** Trường Đại học Ngân hàng TP. Hồ Chí Minh

## Lời cảm ơn

Tôi xin gửi lời cảm ơn đến ông Tô Phúc Hậu, Giám đốc Công ty TNHH IRONTAN VIỆT NAM (IRONTAN VIET NAM COMPANY LIMITED), đã tạo điều kiện và hỗ trợ tôi trong quá trình học tập và nghiên cứu.

Tôi cũng xin bày tỏ lòng biết ơn đến ông Lê Phúc Thịnh, Chủ tịch Hội đồng quản trị và Giám đốc Công ty Cổ phần Đầu tư Phát triển Thương mại Dịch vụ THE MOB GROUP (Deutschfuns LMS), đã đóng góp những ý kiến quý báu và tạo môi trường thuận lợi cho việc ứng dụng các kết quả nghiên cứu. Deutschfuns là nền tảng học tiếng Đức trực tuyến hiện đại tại Việt Nam (https://deutschfuns.com), ứng dụng phương pháp micro learning kết hợp với công nghệ AI, cung cấp đào tạo toàn diện 4 kỹ năng ngôn ngữ từ trình độ A1 đến B1, giúp người học tiếp thu kiến thức nhanh chóng và hiệu quả.

## Tổng quan

Dự án này nghiên cứu việc ứng dụng học máy trong dự đoán khả năng ghi nhớ từ vựng tiếng Anh của học viên, dựa trên phân tích dữ liệu hành vi từ nền tảng học ngôn ngữ Duolingo. Nghiên cứu tập trung vào việc xây dựng các mô hình học máy như Logistic Regression và Random Forest để dự đoán khả năng ghi nhớ từ vựng, từ đó cá nhân hóa quá trình học tập và nâng cao hiệu quả ghi nhớ từ vựng.

## Cấu trúc dự án

```
.
├── docs/                           # Tài liệu
│   └── tieu-luan/                  # Tiểu luận
│       ├── 01-front-matter/        # Phần mở đầu
│       ├── 02-chapters/            # Các chương nội dung
│       ├── 03-back-matter/         # Phần kết thúc
│       └── index.md                # Trang chính
│
└── slam-prediction/                # Mã nguồn
    ├── code/                       # Mã nguồn Python
    │   ├── slam_analysis.py        # Phân tích dữ liệu SLAM
    │   └── visualize_results.py    # Trực quan hóa kết quả
    ├── data/                       # Dữ liệu
    │   └── dataverse_files/        # Dữ liệu gốc
    └── results/                    # Kết quả phân tích
```

## Dữ liệu

Dữ liệu được sử dụng là bộ dữ liệu SLAM (Second Language Acquisition Modeling) từ Duolingo, bao gồm thông tin về hành vi học tập của học viên trong 30 ngày đầu sử dụng ứng dụng. Các đặc trưng chính được sử dụng bao gồm:

-   Số lần thử (num_attempts)
-   Số lần trả lời đúng (num_correct)
-   Thời gian kể từ lần thử cuối (time_since_last_attempt)
-   Các đặc trưng suy ra như thời gian ôn tập và tần suất lặp lại

> **Lưu ý quan trọng**: Do kích thước lớn của bộ dữ liệu SLAM, các file dữ liệu không được đưa vào repository này. Người dùng cần tải bộ dữ liệu từ nguồn chính thức:
>
> Duolingo. (2018). Duolingo SLAM Dataset. Harvard Dataverse. [https://doi.org/10.7910/DVN/N8XJME](https://doi.org/10.7910/DVN/N8XJME)
>
> Sau khi tải về, giải nén và đặt các file vào thư mục `slam-prediction/data/dataverse_files/` để đảm bảo các script phân tích hoạt động chính xác.

## Mô hình

Dự án sử dụng hai mô hình học máy chính:

1. **Logistic Regression**: Mô hình cơ bản với khả năng giải thích cao
2. **Random Forest**: Mô hình phức tạp hơn với độ chính xác cao hơn

## Kết quả

Kết quả nghiên cứu cho thấy cả hai mô hình đều đạt hiệu suất tốt, với độ chính xác khoảng 85.8%. Mô hình Random Forest có hiệu suất nhỉnh hơn một chút (85.82%) so với Logistic Regression (85.80%). Các yếu tố ảnh hưởng quan trọng nhất bao gồm loại bài tập (format_reverse_tap), số lần thử (num_attempts) và tỷ lệ đúng (correct_ratio).

Phân tích tầm quan trọng của đặc trưng cho thấy:

1. **Logistic Regression**:

    - format_reverse_tap: 0.4478
    - num_attempts: 0.3922
    - format_listen: 0.2850
    - correct_ratio: 0.2009

2. **Random Forest**:
    - num_attempts: 0.2059
    - format_reverse_tap: 0.2054
    - correct_ratio: 0.1626
    - format_listen: 0.1100

Kết quả này cho thấy loại bài tập và số lần học viên đã thực hành với một từ vựng cụ thể đóng vai trò quan trọng nhất trong việc dự đoán khả năng ghi nhớ từ vựng.

## Hướng phát triển

Nghiên cứu đề xuất các cải tiến trong tương lai như:

-   Sử dụng dữ liệu dài hạn
-   Áp dụng các kỹ thuật học sâu như RNN hoặc LSTM
-   Phân tích chuỗi dữ liệu hành vi theo thời gian

## Yêu cầu

Để chạy mã phân tích, bạn cần cài đặt các thư viện Python sau:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

### Cài đặt môi trường ảo (Khuyến nghị)

Để tránh xung đột với các dự án Python khác, bạn nên sử dụng môi trường ảo:

```bash
# Tạo môi trường ảo trong thư mục dự án
python -m venv venv

# Kích hoạt môi trường ảo
# Windows:
venv\Scripts\activate
# Linux/Mac:
# source venv/bin/activate

# Cài đặt các thư viện từ file requirements.txt
pip install -r requirements.txt
```

## Các bước thực hiện

### 1. Cài đặt môi trường

```bash
# Clone repository (nếu chưa có)
git clone https://github.com/limpaulfin/HUB-Fong-VocabRetention-ML.git
cd HUB-Fong-VocabRetention-ML

# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
# Windows:
venv\Scripts\activate
# Linux/Mac:
# source venv/bin/activate

# Cài đặt các thư viện
pip install -r requirements.txt
```

### 2. Chuẩn bị dữ liệu

```bash
# Tạo thư mục dữ liệu (nếu chưa có)
mkdir -p slam-prediction/data/dataverse_files

# Tải dữ liệu SLAM từ Duolingo và đặt vào thư mục dataverse_files
# Link: https://doi.org/10.7910/DVN/N8XJME
```

### 3. Phân tích dữ liệu

```bash
# Chạy script phân tích
cd slam-prediction/code
python slam_analysis.py
```

### 4. Trực quan hóa kết quả

```bash
# Tạo các biểu đồ và báo cáo
cd slam-prediction/code
python visualize_results.py
```

### 5. Xem kết quả

Sau khi chạy các script, kết quả sẽ được lưu trong thư mục `slam-prediction/results/`, bao gồm:

-   Các biểu đồ phân tích
-   Báo cáo kết quả
-   Mô hình đã huấn luyện

## Tài liệu tham khảo

-   Settles, B., Brust, C., Gustafson, E., Hagiwara, M., & Madnani, N. (2018). Second Language Acquisition Modeling. In Proceedings of the NAACL-HLT Workshop on Innovative Use of NLP for Building Educational Applications (BEA). ACL.
-   Duolingo. (2018). Duolingo SLAM Dataset. Harvard Dataverse. https://doi.org/10.7910/DVN/N8XJME
