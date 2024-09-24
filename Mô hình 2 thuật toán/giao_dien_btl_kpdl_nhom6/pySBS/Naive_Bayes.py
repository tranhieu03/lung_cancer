import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Đọc dữ liệu từ tập tin CSV
data = pd.read_csv(r'C:\Users\tranx\Downloads\train.csv')

# Chia dữ liệu thành features (đặc trưng) và labels (nhãn)
X = data.iloc[:, :-1]  # Tất cả các cột trừ cột cuối cùng
y = data.iloc[:, -1]   # Chỉ cột cuối cùng

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình Naive Bayes
model = GaussianNB()

# Huấn luyện mô hình
model.fit(X_train, y_train)

# Dự đoán nhãn cho dữ liệu kiểm tra
y_pred = model.predict(X_test)

# Đánh giá độ chính xác của mô hình
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

joblib.dump(model, 'naive_bayes_model.joblib')
