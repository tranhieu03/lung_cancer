import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('dt2.csv')

# Thực hiện sửa đổi
df['LUNG_CANCER'] = df['LUNG_CANCER'].apply(lambda x: x.capitalize() if x.upper() in ['HIGH', 'LOW'] else x)

# Lưu dữ liệu đã sửa vào file CSV
df.to_csv('dt2_sua.csv', index=False)