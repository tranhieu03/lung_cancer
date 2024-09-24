import tkinter as tk
from tkinter import ttk
import joblib

def update_age_label(event=None):
    """Cập nhật giá trị tuổi hiển thị khi người dùng di chuyển thanh điều chỉnh."""
    age_value = age_var.get()
    age_label.config(text=f"{age_value}")

def submit_form():
    # Lấy dữ liệu từ các ô nhập liệu
    data = []
    for var in variable_list:
        if var == age_var:
            # Lấy giá trị từ thanh điều chỉnh
            data.append(float(var.get()))
        elif var == gender_var:
            # Chuyển đổi giá trị giới tính thành số
            value = 1 if var.get() == 'Nam' else 2
            data.append(value)
        else:
            data.append(float(var.get()))

    data = [data]

    # Hiển thị dữ liệu đã nhập
    print("Dữ liệu đã nhập:")
    for i, value in enumerate(data):
        print(f"Ô {i + 1}: {value}")

    # Tải mô hình từ tệp
    model = joblib.load('Decision_tree.joblib')

    # Dự đoán trên tập dữ liệu
    y_pred = model.predict(data)
    if y_pred[0] == 3:
        result_label.config(text="Nặng", fg="red")
    elif y_pred[0] == 2:
        result_label.config(text="Vừa", fg="yellow")
    else:
        result_label.config(text="Nhẹ", fg="blue")

# Tạo cửa sổ
root = tk.Tk()
root.title("Form Nhập Dữ Liệu")

# Thiết lập kích thước cửa sổ
root.geometry("400x400")

# Tạo danh sách các giá trị từ 1 đến 9
value_list = list(range(1, 10))

# Tạo danh sách các tên riêng biệt cho các ô nhập liệu
field_names = [
    "Giới tính",
    "Tuổi",
    "Hút thuốc",
    "Đồ uống cồn",
    "Dị ứng",
    "Bệnh mãn tính",
    "Mệt mỏi",
    "Đau ngực",
    "Thở dốc",
    "rên rỉ",
    "Nuốt nước bọt khó",
    "Ho"
]

# Tạo danh sách các biến để lưu giá trị được chọn từ dropdown list
variable_list = []
gender_var = tk.StringVar(value="Nam")

# Tạo ô nhập liệu cho giới tính
label = tk.Label(root, text="Giới tính:")
label.grid(row=0, column=0, padx=10, pady=5)
combobox = ttk.Combobox(root, textvariable=gender_var, values=["Nam", "Nữ"])
combobox.grid(row=0, column=1, padx=10, pady=5)
variable_list.append(gender_var)

# Tạo ô nhập liệu tuổi bằng thanh điều chỉnh
age_var = tk.IntVar(value=25)  # Giá trị mặc định là 25
label = tk.Label(root, text="Tuổi:")
label.grid(row=1, column=0, padx=10, pady=5)

# Tạo thanh điều chỉnh tuổi
age_scale = ttk.Scale(root, from_=1, to=100, variable=age_var, orient="horizontal", command=update_age_label)
age_scale.grid(row=1, column=1, padx=10, pady=5)

# Tạo nhãn hiển thị giá trị tuổi đang chọn
age_label = tk.Label(root, text=f"{age_var.get()}")
age_label.grid(row=1, column=2, padx=10, pady=5)

# Thêm thanh điều chỉnh tuổi vào danh sách biến
variable_list.append(age_var)

# Tạo các ô nhập liệu khác
for i, name in enumerate(field_names[2:], start=2):
    label = tk.Label(root, text=f"{name}:")
    label.grid(row=i, column=0, padx=10, pady=5)
    # Tạo biến StringVar để lưu giá trị được chọn
    var = tk.StringVar(value="1")  # Giá trị mặc định là 1
    dropdown = ttk.OptionMenu(root, var, value_list[0], *value_list)
    dropdown.grid(row=i, column=1, padx=10, pady=5)
    variable_list.append(var)

# Tạo nút "Submit" để gửi dữ liệu
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=16, column=0, columnspan=2, pady=10)

# Kết quả dự đoán
result_label = tk.Label(root, text="Kết quả dự đoán:")
result_label.grid(row=17, column=0, columnspan=2, pady=10)

# Khởi động giao diện người dùng
root.mainloop()
