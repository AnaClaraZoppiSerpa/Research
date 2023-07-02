import pprint
import csv
import math
import heapq
import sys

XTIME_WEIGHT=3
XOR_WEIGHT=1

class Datapoint:
    def __init__(self, csv_row):
        self.year, self.dim, self.mat_type, self.involutory, self.use, self.paper, self.field_power, self.poly, self.xor, self.ixor, self.xtime, self.ixtime, self.mat_id, self.mat_inv_id, self.why_empty, self.obs = csv_row

        if self.xtime == '---':
            self.xtime = 0
        if self.xor == '---':
            self.xor = 0

        self.dim = int(self.dim)
        self.xtime = int(self.xtime)
        self.xor = int(self.xor)
    
    def cost_formula_1xtime_equals_3xor(self):
        return XTIME_WEIGHT * self.xtime + XOR_WEIGHT * self.xor

def get_datapoint_list_from_csv():
    csv_filename = 'complete_table_with_all_matrices_and_instances_backup.csv'  # Replace with your CSV file path
    csv_rows = read_csv(csv_filename)
    csv_rows = csv_rows[1:]

    datapoint_objects = []
    datapoints_as_dicts = []

    for row in csv_rows:
        datapoint = Datapoint(row)
        datapoint_objects.append(datapoint)
        datapoints_as_dicts.append(datapoint.__dict__)
    
    return datapoint_objects, datapoints_as_dicts

def group_by_dimension(datapoints):
    dim_dict = {}

    for datapoint in datapoints:
        if datapoint.dim in dim_dict:
            dim_dict[datapoint.dim].append(datapoint)
        else:
            dim_dict[datapoint.dim] = [datapoint]
    
    return dim_dict


def group_by_dimension_as_dict(datapoints):
    dim_dict = {}

    for datapoint in datapoints:
        if datapoint.dim in dim_dict:
            dim_dict[datapoint.dim].append(datapoint.__dict__)
        else:
            dim_dict[datapoint.dim] = [datapoint.__dict__]

    return dim_dict

def group_by_field_and_dimension():
    # TO-DO
    pass

def find_cheapest_from_dimension_according_to_encryption_cost(dim_dict):
    cheapest = {}
    dimension_min_cost = {}

    for dimension in dim_dict:
        cheapest[dimension] = []
        min_cost = math.inf
        for datapoint in dim_dict[dimension]:
            cost = datapoint.cost_formula_1xtime_equals_3xor()
            #print(datapoint.mat_id, cost)
            if (cost <= min_cost and cost > 0):
                min_cost = cost
        
        dimension_min_cost[dimension] = min_cost

        for datapoint in dim_dict[dimension]:
            cost = datapoint.cost_formula_1xtime_equals_3xor()
            if cost == min_cost:
                cheapest[dimension].append(datapoint)
    
    return cheapest, dimension_min_cost


def read_csv(filename):
    rows = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)
    return rows

# Filter by dimension
# Filter by field_power
# Get top k according to formula involving xtime and xor

def filter_by_dimension(dataset, dimension):
    if dimension in dataset:
        return dataset[dimension]
    return {}

def filter_by_field_power(dataset, field_power):
    return list(filter(lambda d: d.get("field_power") == field_power, dataset))

def filter_by_id_substring(dataset, id_substring):
    return list(filter(lambda d: id_substring in d.get("mat_id"), dataset))

def get_top_k_according_to_formula(dataset, formula, k):
    return heapq.nsmallest(k, dataset, key=formula)

def formula_3xtime_1xor(datapoint):
    if datapoint["xtime"] == 0 or datapoint["xor"] == 0:
        return math.inf

    return 3 * datapoint["xtime"] + datapoint["xor"]

def formula_xt_only(datapoint):
    if datapoint["xtime"] == 0 or datapoint["xor"] == 0:
        return math.inf
    return datapoint["xtime"]


def formula_duwal_3xtime_1xor(datapoint):
    if datapoint["xtime"] == 0 or datapoint["xor"] == 0:
        return math.inf

    if datapoint["ixtime"] == "---" or datapoint["ixor"] == "---":
        return math.inf

    return 3 * int(datapoint["ixtime"]) + int(datapoint["ixor"])


def formula_duwal_xt_only(datapoint):
    if datapoint["xtime"] == 0 or datapoint["xor"] == 0:
        return math.inf

    if datapoint["ixtime"] == "---" or datapoint["ixor"] == "---":
        return math.inf

    return int(datapoint["ixtime"])

def get_dataset():
    objs, dicts = get_datapoint_list_from_csv()
    return group_by_dimension_as_dict(objs)

def query(dataset, dimension, field_power=None, substring=None, formula=None, k=None):
    filtered = filter_by_dimension(dataset, dimension)
    if field_power:
        filtered = filter_by_field_power(filtered, field_power)
    if substring:
        filtered = filter_by_id_substring(filtered, substring)
    if formula:
        if k:
            filtered = get_top_k_according_to_formula(filtered, formula, k)
    return filtered

def cheapest_per_dim_beierle():
    print("beierle")
    print("xt-only")
    print("=======")
    for dim in range(2, 32+1):
        res = query(get_dataset(), dim, substring="beierle", formula=formula_xt_only, k=10)
        if len(res):
            print("dim =", dim)
            cprint(res)

    print("3:1")
    print("=======")
    for dim in range(2, 32+1):
        res = query(get_dataset(), dim, substring="beierle", formula=formula_3xtime_1xor, k=10)
        if len(res):
            print("dim =", dim)
            cprint(res)

def cheapest_per_dim_duwal():
    print("duwal")
    print("xt-only")
    print("=======")
    for dim in range(2, 32+1):
        res = query(get_dataset(), dim, substring="duwal", formula=formula_xt_only, k=10)
        if len(res):
            print("dim =", dim)
            cprint(res)

    print("3:1")
    print("=======")
    for dim in range(2, 32+1):
        res = query(get_dataset(), dim, substring="duwal", formula=formula_3xtime_1xor, k=10)
        if len(res):
            print("dim =", dim)
            cprint(res)

def cheapest_per_dim_all():
    print("all")
    print("xt-only")
    print("=======")
    for dim in range(2, 32+1):
        res = query(get_dataset(), dim, formula=formula_xt_only, k=10)
        if len(res):
            print("dim =", dim)
            cprint(res)

    print("3:1")
    print("=======")
    for dim in range(2, 32+1):
        res = query(get_dataset(), dim, formula=formula_3xtime_1xor, k=10)
        if len(res):
            print("dim =", dim)
            cprint(res)

def cprint(results):
    for res in results:
        print(res["mat_id"], res["xtime"], res["xor"], res["ixtime"], res["ixor"])

def full_table_for_dim_and_sub(dim, sub=None):
    initial_dataset = get_dataset()
    res_xt_only = query(initial_dataset, dim, substring=sub, formula=formula_duwal_xt_only, k=20)
    res_3xt_1xr = query(initial_dataset, dim, substring=sub, formula=formula_duwal_3xtime_1xor, k=20)

    #rows = [["dim","mat_id", "xtime1", "xor1", "ixtime1", "ixor1", "xtime2", "xor2", "ixtime2", "ixor2"]]
    rows = []
    for i in range(10):
        if i < len(res_xt_only):
            a = res_xt_only[i]
            b = res_3xt_1xr[i]
            row_a = [dim, a["mat_id"], a["xtime"], a["xor"], a["ixtime"], a["ixor"], a["involutory"]]
            row_b = [b["mat_id"], b["xtime"], b["xor"], b["ixtime"], b["ixor"], b["involutory"]]
            full_row = row_a + row_b
            rows.append(full_row)

    return rows

print(query(get_dataset(), 3, substring="duwal", formula=formula_duwal_3xtime_1xor, k=10))