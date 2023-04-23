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
    new_rows = []
    with open("selected_cols.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cols = row[0].split(";")

            #print(cols)

            dim = cols[0]
            paper = cols[1]
            field = cols[2]
            xor_ixor = cols[3]
            xtime_ixtime = cols[4]
            id_iid = cols[5]

            if "\\\\" in xor_ixor:
                xor, ixor = xor_ixor.split("\\\\")
            else:
                xor = xor_ixor
                ixor = "*"
            
            if "\\\\" in xtime_ixtime:
                xtime, ixtime = xtime_ixtime.split("\\\\")
            else:
                xtime = xtime_ixtime
                ixtime = "*"
            
            print(dim, paper, field, xor, ixor, xtime, ixtime, id_iid)
            new_row = [dim, paper, field, xor, ixor, xtime, ixtime, id_iid]
            new_rows.append(new_row)
    
    with open("split_costs.csv", "w") as h:
        write = csv.writer(h)
        write.writerows(new_rows)

def filtered_table_2():
    id_rows = []
    with open("split_costs_2.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            mat_id = row[7]

            id = mat_id
            inv_id = ""

            if "\\\\" in mat_id:
                id, inv_id = mat_id.split("\\\\")
                id_row = [id, inv_id]
                id_rows.append(id_row)
    
    with open("split_ids.csv", "w") as h:
        write = csv.writer(h)
        write.writerows(id_rows)
            

filtered_table_2()