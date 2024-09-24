import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
data = pd.read_csv(r'C:\Users\tranx\Downloads\du_lieu_moi_500_1000.csv')

# Xác định đầu vào (features) và nhãn (label)
X = data[['AGE', 'GENDER', 'ALCOHOL', 'ALLERGY', 'CHRONIC_DISEASE', 'SMOKING', 'CHESTPAIN', 'FATIGUE', 'SHORTNESS_OF_BREATH', 'SWALLOWING_DIFFICULTY', 'COUGHING']]
y = data['LUNG_CANCER']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Khởi tạo và huấn luyện mô hình Decision Tree
dtree = DecisionTreeClassifier(random_state=1)
dtree.fit(X_train, y_train)

# Dự đoán kết quả cho tập kiểm tra
y_pred = dtree.predict(X_test)

# Tạo ma trận nhầm lẫn
cm = confusion_matrix(y_test, y_pred)

# Tính toán Accuracy, Precision, Recall, F1-score
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='macro')
recall = recall_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

# Hiển thị ma trận nhầm lẫn bằng seaborn
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# In kết quả tính toán
print(f'Accuracy: {accuracy:.4f}')
print(f'Precision: {precision:.4f}')
print(f'Recall: {recall:.4f}')
print(f'F1-score: {f1:.4f}')

# In báo cáo phân loại
report = classification_report(y_test, y_pred)
print('Classification Report:')
print(report)
