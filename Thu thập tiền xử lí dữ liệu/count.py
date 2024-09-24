import pandas as pd
import sys
# Thay đổi mã hóa mặc định của hệ thống sang utf-8
sys.stdout.reconfigure(encoding='utf-8')

# Đọc dữ liệu từ tệp CSV ban đầu
df_original = pd.read_csv('lung_cancer(2).csv')

# Đếm số lượng bản ghi ban đầu
original_count = len(df_original)

# In số lượng bản ghi ban đầu
print(f'Số lượng bản ghi ban đầu: {original_count}')

# Đọc dữ liệu từ tệp CSV sau khi đã được làm sạch và lọc trùng
df_cleaned = pd.read_csv('LungCancer_cleaned(1).csv')

# Đếm số lượng bản ghi sau khi lọc trùng
cleaned_count = len(df_cleaned)

# In số lượng bản ghi sau khi lọc trùng
print(f'Số lượng bản ghi sau khi lọc trùng: {cleaned_count}')