import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Đọc dữ liệu từ tập tin CSV
data = pd.read_csv(r'C:\Users\tranx\Downloads\train.csv')

# Xác định các đặc trưng và nhãn
X = data.iloc[:, :-1]  # Loại bỏ cột nhãn đểapp lấy các đặc trưng
Y = data.iloc[:, -1]  # Nhãn

# Phân chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Xây dựng mô hình cây quyết định ID3
model = DecisionTreeClassifier(criterion='entropy')  # Sử dụng ID3 với entropy làm tiêu chí chia
model.fit(X_train, y_train)


# Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá độ chính xác của mô hình
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Lưu mô hình đã huấn luyện
joblib.dump(model, 'ID3.pkl')