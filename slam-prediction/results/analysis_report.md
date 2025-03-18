# Báo cáo phân tích dữ liệu SLAM

## 1. Kết quả đánh giá mô hình

### Logistic Regression

- Accuracy: 0.8580
- Precision: 0.5000
- Recall: 0.0021
- F1 Score: 0.0042
- ROC AUC: 0.6917

### Random Forest

- Accuracy: 0.8582
- Precision: 0.8750
- Recall: 0.0019
- F1 Score: 0.0038
- ROC AUC: 0.7165

## 2. Tầm quan trọng của đặc trưng

### Logistic Regression

| Đặc trưng | Tầm quan trọng |
|-----------|---------------|
| format_reverse_tap | 0.4478 |
| num_attempts | 0.3922 |
| format_listen | 0.2850 |
| correct_ratio | 0.2009 |
| pos_PRON | 0.1436 |
| format_reverse_translate | 0.1161 |
| pos_ADJ | 0.0945 |
| pos_NOUN | 0.0888 |
| pos_ADV | 0.0642 |
| pos_ADP | 0.0618 |

### Random Forest

| Đặc trưng | Tầm quan trọng |
|-----------|---------------|
| num_attempts | 0.2059 |
| format_reverse_tap | 0.2054 |
| correct_ratio | 0.1626 |
| format_listen | 0.1100 |
| days | 0.0960 |
| time_since_last_attempt | 0.0519 |
| format_reverse_translate | 0.0510 |
| pos_PRON | 0.0285 |
| pos_ADJ | 0.0198 |
| pos_DET | 0.0173 |

## 3. Tương quan giữa các đặc trưng

| Đặc trưng | num_attempts | correct_ratio | time_since_last_attempt | days | target |
|-----------|--------------|---------------|-------------------------|------|--------|
| num_attempts | 1.00 | 0.05 | 0.03 | 0.08 | -0.09 |
| correct_ratio | 0.05 | 1.00 | 0.06 | 0.01 | 0.08 |
| time_since_last_attempt | 0.03 | 0.06 | 1.00 | 0.09 | -0.02 |
| days | 0.08 | 0.01 | 0.09 | 1.00 | 0.00 |
| target | -0.09 | 0.08 | -0.02 | 0.00 | 1.00 |

## 4. Kết luận

- Mô hình Random Forest có hiệu suất tốt hơn Logistic Regression trong việc dự đoán khả năng ghi nhớ từ vựng.
- Đặc trưng quan trọng nhất theo Logistic Regression là 'format_reverse_tap'.
- Đặc trưng quan trọng nhất theo Random Forest là 'num_attempts'.

- Các đặc trưng có tương quan mạnh nhất với khả năng ghi nhớ từ vựng:
  - correct_ratio: 0.08
  - days: 0.00
  - time_since_last_attempt: -0.02
  - num_attempts: -0.09
