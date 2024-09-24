import pandas as pd

# Đọc file CSV vào DataFrame
df = pd.read_csv('du_lieu_moi_xxx.csv')

# Đổi tên các cột
df.rename(columns={'Gender': 'GENDER', 'Age': 'AGE',
                   'Alcoholuse':'ALCOHOL','DustAllergy':'ALLERGY',
                   'chronicLungDisease':'CHRONIC DISEASE',
                   'Smoking':'SMOKING','ChestPain':'CHESTPAIN'
                   ,'Fatigue':'FATIGUE','ShortnessofBreath':'SHORTNESS_OF_BREATH',
                   'Wheezing':'WHEEZING','SwallowingDifficulty':'SWALLOWING DI22ICULTY',
                   'DryCough':'COUGHING','Level':'LUNG_CANCER'
                   
                   
                   }, inplace=True)

# Lưu DataFrame với các cột đã được đổi tên vào file CSV mới
df.to_csv('dt1_doi_ten.csv', index=False)


#ndex,Age,Gender,'Air Pollution','Alcohol use','Dust Allergy','OccuPational Hazards','Genetic Risk','chronic Lung Disease','Balanced Diet',Obesity,Smoking,'Passive Smoker','Chest Pain','Coughing of Blood',Fatigue,'Weight Loss','Shortness of Breath',Wheezing,'Swallowing Difficulty','Clubbing of Finger Nails','Frequent Cold','Dry Cough',Snoring,Level
