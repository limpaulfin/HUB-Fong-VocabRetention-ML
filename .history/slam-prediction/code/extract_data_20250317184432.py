"""
File: extract_data.py
Danh sách file liên quan/phụ thuộc:
- ../data/dataverse_files/data_en_es.tar
- ../data/dataverse_files/data_es_en.tar
- ../data/dataverse_files/data_fr_en.tar
- ../data/dataverse_files/starter_code.tar

Chức năng chính và mục đích của file:
- Giải nén dữ liệu SLAM từ các file tar
- Chuẩn bị dữ liệu cho quá trình phân tích
"""

import os
import tarfile
import shutil

def extract_tar_file(tar_path, extract_path):
    """Giải nén file tar vào thư mục đích"""
    print(f"Đang giải nén {tar_path}...")

    # Kiểm tra xem file tar có tồn tại không
    if not os.path.exists(tar_path):
        print(f"Lỗi: File {tar_path} không tồn tại!")
        return False

    # Tạo thư mục đích nếu chưa tồn tại
    os.makedirs(extract_path, exist_ok=True)

    try:
        # Giải nén file tar
        with tarfile.open(tar_path, 'r') as tar:
            tar.extractall(path=extract_path)
        print(f"Đã giải nén thành công {tar_path} vào {extract_path}")
        return True
    except Exception as e:
        print(f"Lỗi khi giải nén {tar_path}: {str(e)}")
        return False

def main():
    # Thư mục chứa dữ liệu
    data_dir = "../data/dataverse_files"

    # Danh sách các file tar cần giải nén
    tar_files = [
        "data_en_es.tar",
        "data_es_en.tar",
        "data_fr_en.tar",
        "starter_code.tar"
    ]

    # Thư mục đích để giải nén
    extract_dir = "../data/extracted_data"

    # Tạo thư mục đích nếu chưa tồn tại
    os.makedirs(extract_dir, exist_ok=True)

    # Giải nén từng file tar
    for tar_file in tar_files:
        tar_path = os.path.join(data_dir, tar_file)
        extract_path = os.path.join(extract_dir, os.path.splitext(tar_file)[0])

        # Xóa thư mục đích nếu đã tồn tại
        if os.path.exists(extract_path):
            print(f"Xóa thư mục {extract_path} đã tồn tại...")
            shutil.rmtree(extract_path)

        # Giải nén file tar
        success = extract_tar_file(tar_path, extract_path)

        if success:
            print(f"Đã giải nén thành công {tar_file}")
        else:
            print(f"Không thể giải nén {tar_file}")

    print("\nQuá trình giải nén hoàn tất!")
    print("Dữ liệu đã được giải nén vào thư mục:", extract_dir)
    print("\nCấu trúc thư mục sau khi giải nén:")
    print("../data/extracted_data/")
    print("├── data_en_es/")
    print("├── data_es_en/")
    print("├── data_fr_en/")
    print("└── starter_code/")

if __name__ == "__main__":
    main()
