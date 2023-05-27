import pprint
import csv
import math

XTIME_WEIGHT=3
XOR_WEIGHT=1

class Datapoint:
    def __init__(self, csv_row):
        self.year, self.dim, self.mat_type, self.involutory, self.use, self.paper, self.field_power, self.poly, self.xor, self.ixor, self.xtime, self.ixtime, self.mat_id, self.mat_inv_id, self.why_empty, self.obs = csv_row

        if self.xtime == '---': self.xtime = 0
        if self.xor == '---': self.xor = 0

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

def test():
    objs, dicts = get_datapoint_list_from_csv()
    dim_dict = group_by_dimension(objs)
    
    #for key in dim_dict:
    #    print(key)
    #    for d in dim_dict[key]:
    #        print("-", d.mat_id)

    cheapest, dim_baselines = find_cheapest_from_dimension_according_to_encryption_cost(dim_dict)

    #for dim in cheapest:
    #    print("dim =", dim)
    #    for mat in cheapest[dim]:
    #        print(mat.mat_id, ",", mat.cost_formula_1xtime_equals_3xor())

    for dim in cheapest:
        print("dim =", dim, "mat count =", len(cheapest[dim]), "cost =", dim_baselines[dim])

test()
