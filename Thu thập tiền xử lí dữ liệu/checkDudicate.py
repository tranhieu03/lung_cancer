import pandas as pd

# Đọc dữ liệu từ file CSV vào DataFrame
df = pd.read_csv('lung_cancer(2).csv')

# Điền các giá trị còn thiếu bằng giá trị mặc định (ví dụ: 'Unknown' hoặc 0)
df.fillna({'Age': '24'}, inplace=True)
df.fillna({'Gender': '1'}, inplace=True)
df.fillna({'Air Pollution': '3'}, inplace=True)
df.fillna({'Alcohol use': '2'}, inplace=True)
df.fillna({'Dust Allergy': '2'}, inplace=True)
df.fillna({'OccuPational Hazards': '4'}, inplace=True)
df.fillna({'Genetic Risk': '4'}, inplace=True)
df.fillna({'chronic Lung Disease': '2'}, inplace=True)
df.fillna({'Balanced Diet': '4'}, inplace=True)
df.fillna({'Obesity,Smoking': '2'}, inplace=True)
df.fillna({'Passive Smoker': '4'}, inplace=True)
df.fillna({'Chest Pain': '2'}, inplace=True)
df.fillna({'Coughing of Blood': '4'}, inplace=True)
df.fillna({'Fatigue,Weight Loss': '2'}, inplace=True)
df.fillna({'Shortness of Breath': '4'}, inplace=True)
df.fillna({'Wheezing': '2'}, inplace=True)
df.fillna({'Swallowing Difficulty': '4'}, inplace=True)
df.fillna({'Clubbing of Finger Nails': '2'}, inplace=True)
df.fillna({'Frequent Cold': '4'}, inplace=True)
df.fillna({'Dry Cough': '2'}, inplace=True)
df.fillna({'Snoring': '4'}, inplace=True)
#df.fillna({'Age': '24'}, inplace=True)
#df.fillna({'Age': '24'}, inplace=True)
df.fillna({'level': 'MEDIUM'}, inplace=True)

# Kiểm tra và xóa các bản ghi trùng nhau dựa trên tất cả các cột
df.drop_duplicates(inplace=True)

# Lưu DataFrame đã được xử lý vào file CSV mới
df.to_csv('LungCancer_cleaned(1).csv', index=False)
