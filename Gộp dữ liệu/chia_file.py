import csv

def split_csv(input_file, output_file1, output_file2, split_ratio=0.8):
    with open(input_file, 'r', newline='') as infile, \
         open(output_file1, 'w', newline='') as outfile1, \
         open(output_file2, 'w', newline='') as outfile2:
        
        reader = csv.reader(infile)
        writer1 = csv.writer(outfile1)
        writer2 = csv.writer(outfile2)
        
        headers = next(reader)
        writer1.writerow(headers)
        writer2.writerow(headers)
        
        total_rows = sum(1 for row in reader)
        split_index = int(total_rows * split_ratio)
        
        infile.seek(0)  # reset file pointer to beginning
        
        for i, row in enumerate(reader):
            if i < split_index:
                writer1.writerow(row)
            else:
                writer2.writerow(row)

# Sử dụng hàm để chia file CSV
split_csv('du_lieu_moi_500_1000_xoacotthua.csv', 'train.csv', 'test.csv', 0.8)
