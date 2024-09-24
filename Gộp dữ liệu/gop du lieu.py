import pandas as pd

# Đọc hai tệp CSV
df1 = pd.read_csv('dt1_doi_ten.csv')
df2 = pd.read_csv('dt2_in_output.csv')

# Gộp hai DataFrame lại với nhau
df_combined = pd.concat([df1, df2], ignore_index=True)

# Lưu kết quả vào một tệp CSV mới
df_combined.to_csv('dt1_2.csv', index=False)
