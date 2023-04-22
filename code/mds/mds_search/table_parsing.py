import csv

data_rows = []

def full_table():
    with open("report_table1.txt", "r") as f:
        content = f.read()
        lines = content.split("\hline")
        
        for l in lines:
            data = l.split("&")
            data_rows.append(data)
            
    with open("table_csv.csv", "w") as h:
        write = csv.writer(h)
        write.writerows(data_rows)

def filtered_table():
    with open("selected_cols.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

filtered_table()