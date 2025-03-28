# Download GOPRO.pkl
https://drive.google.com/drive/folders/1OJv9d6e90hlpDSyo8oJY-END3xj4nUmg

# Hide
link to data: https://drive.google.com/file/d/13CoUG0YktPGzVagOipoo43NMZclOG7J2/view
run:run: !python main.py --data HIDE --mode test --data_dir path to data --test_model path to model --save_image True 

# RealBlur-R
link to data: https://www.kaggle.com/datasets/jishnuparayilshibu/a-curated-list-of-image-deblurring-datasets
run: !python main.py --data RBLUR-R --mode test --data_dir path to data --test_model path to model --save_image True 

# File SFNet_deblur.ipynb là file chạy các tập dữ liệu

# Để chạy tập HIDE của bài báo
zip_path = "/content/drive/MyDrive/SFNet/HIDE.zip" # đổi thành HIDE hoặc RealBlur_J
extract_path = "/content/SFNet/Motion_deblurring/data/"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Giải nén thành công!")
old_folder = "/content/SFNet/Motion_deblurring/data/HIDE"
new_folder = "/content/SFNet/Motion_deblurring/data/test"

os.rename(old_folder, new_folder)
print("Đã đổi tên thư mục thành công!")

!python main.py --data HIDE --mode test --data_dir /content/SFNet/Motion_deblurring/data/test --test_model /content/drive/MyDrive/SFNet/GOPRO.pkl --save_image True


# Để chạy tập RealBlur_R
zip_path = "/content/drive/MyDrive/SFNet/RealBlur_R.zip" # đổi thành HIDE hoặc RealBlur_J
extract_path = "/content/SFNet/Motion_deblurring/data/"


with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Giải nén thành công!")


!python main.py --data HIDE --mode test --data_dir /content/SFNet/Motion_deblurring/data/RealBlur_R/test --test_model /content/drive/MyDrive/SFNet/GOPRO.pkl --save_image True

# Để chạy tập RealBlur_J
zip_path = "/content/drive/MyDrive/SFNet/RealBlur_J.zip" # đổi thành HIDE hoặc RealBlur_J
extract_path = "/content/SFNet/Motion_deblurring/data/"


with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Giải nén thành công!")


!python main.py --data HIDE --mode test --data_dir /content/SFNet/Motion_deblurring/data/RealBlur_J/test --test_model /content/drive/MyDrive/SFNet/GOPRO.pkl --save_image True