import csv

def replace_values(input_file, output_file, old_value, new_value):
    with open(input_file, 'r', newline='') as infile, \
         open(output_file, 'w', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            first_column = row[0]  # Giữ nguyên giá trị của cột đầu
            modified_row = [first_column]  # Tạo list mới với giá trị của cột đầu
            
            for cell in row[1:]:  # Duyệt qua các giá trị của các cột còn lại
                if cell == old_value:
                    modified_row.append(new_value)  # Thay đổi giá trị nếu cần
                else:
                    modified_row.append(cell)  # Giữ nguyên giá trị nếu không cần thay đổi
            
            writer.writerow(modified_row)

# Sử dụng hàm để thay đổi giá trị
replace_values('dt2_sua_output.csv', 'dt2_inoutput.csv', '2', '8')

