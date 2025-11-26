import os
from pathlib import Path
import logging

# Cấu hình logging ngay từ đầu
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

list_of_paths = [
    ".github/workflows/.gitkeep", #Thư mục chứa các file CI/CD (tự động test, deploy khi push code)
    "src/__init__.py", # File khởi tạo package src
    "src/components/__init__.py",#Package con chứa các thành phần chính
    "src/components/data_ingestion.py", # Component tải dữ liệu (từ CSV, API, database…)
    "src/components/data_transformation.py",# Làm sạch, xử lý dữ liệu, tạo feature
    "src/components/model_trainer.py", # Huấn luyện mô hình ML
    "src/components/model_evaluation.py", # Đánh giá hiệu suất mô hình
    
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py", # Pipeline tổng thể để train từ A-Z
    "src/pipelines/prediction_pipeline.py", # Pipeline để dự đoán với mô hình đã train
    
    "src/utils/__init__.py", # Chứa các hàm tiện ích chung (logger, save/load model, v.v.)
    "src/utils/utils.py", 
    "src/logger/logging.py", # Cấu hình hệ thống logging cho project
    "src/exception/exception.py", # Xử lý ngoại lệ tùy chỉnh cho project
  
    # MongoDB files
    "src/database/__init__.py", # Package cho database operations
    "src/database/mongodb.py", # Kết nối và thao tác với MongoDB
    "src/database/mongodb_operations.py", # Các hàm CRUD cho MongoDB
    "src/database/mongodb_models.py", # Định nghĩa schema/models cho MongoDB documents
    "src/database/mongodb_connection.py", # Quản lý kết nối MongoDB
    
    "tests/unit/__init__.py", # Test từng hàm nhỏ (unit test)
    "tests/integration/__init__.py", # Test cả pipeline chạy từ đầu đến cuối
    
    "init_setup.sh", # Script khởi tạo môi trường (cài đặt thư viện, biến môi trường)
    "requirements.txt", # Thư viện cần thiết để chạy project
    "requirements_dev.txt", # Thư viện chỉ dùng khi phát triển (pytest, black, jupyter…)
    "setup.py", # File cấu hình package Python
    "setup.cfg", # File cũ để đóng gói project thành package pip
    "pyproject.toml", # File hiện đại hơn (dùng với poetry hoặc setuptools mới)
    "tox.ini", # Công cụ chạy test trên nhiều phiên bản Python
    
    "experiment/experiments.ipynb", # Notebook để thử nghiệm, khám phá dữ liệu ban đầu
    
    #Thêm file cấu hình thường dùng
    ".gitignore",
    "README.md",
    "LICENSE",
    "config/config.yaml",                            # File config (rất hay dùng)
    "params.yaml",                                   # Hyperparameters
    "dvc.yaml",                                      # Nếu dùng DVC (Data Version Control)
    "notebooks/exploratory_data_analysis.ipynb",    # Notebook EDA riêng
    
]


for filepath in list_of_paths:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    # Tạo thư mục nếu chưa tồn tại
    if filedir != Path("."):
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir}")

    # Tạo file rỗng nếu chưa tồn tại hoặc file rỗng
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

print("Tất cả thư mục và file đã được tạo thành công!")