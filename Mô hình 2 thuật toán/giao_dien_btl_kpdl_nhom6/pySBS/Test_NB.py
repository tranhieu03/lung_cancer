import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

# Đọc dữ liệu từ tập tin CSV
data = pd.read_csv(r'C:\Users\tranx\Downloads\test.csv')

# Xác định các đặc trưng và nhãn
X = data.iloc[:, :-1].values  # Loại bỏ cột nhãn để lấy các đặc trưng
y = data.iloc[:, -1].values  # Nhãn

# Load mô hình đã được huấn luyện
# model = joblib.load('ID3.pkl')
model = joblib.load('naive_bayes_model.joblib.joblib')

# Dự đoán trên tập dữ liệu
y_pred = model.predict(X)

# Đánh giá độ chính xác của mô hình
accuracy = model.score(X, y)
print("Accuracy:", accuracy)