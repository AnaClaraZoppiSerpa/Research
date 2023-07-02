import csv
import re

pattern = r"_alpha_\d+"

def get_duwal_poly(string):
    prefix = "_int_"
    start_index = string.index(prefix) + len(prefix)

    return string[start_index:]

def get_only_id(string):
    prefix = "_int_"
    start_index = string.index(prefix)

    id = "mat:" + string[:start_index]
    id.replace("_", "-")
    return "\eqref{" + id + "}"
def csv_to_latex(csv_file):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        headers.append("Irreducible Poly")

        # Generate the LaTeX table header
        latex_table = "\\begin{longtable}{|" + "|".join(["c"] * len(headers)) + "|}\n"
        latex_table += "\\hline\n"
        latex_table += " & ".join(headers) + " \\\\\n"
        latex_table += "\\hline\n"
        latex_table += "\\endfirsthead\n"
        latex_table += "\\hline\n"
        latex_table += " & ".join(headers) + " \\\\\n"
        latex_table += "\\hline\n"
        latex_table += "\\endhead\n"
        latex_table += "\\hline\n"
        latex_table += "\\endfoot\n"

        # Generate the table rows
        row_count = 0

        for row in reader:
            row_values = []
            for header in headers:
                if "_alpha_" in row[header]:
                    row[header] = re.sub(pattern, "", row[header])
                    row[header] = "\eqref{mat:" + row[header] + "}"

                if "duwal" in row[header]:
                    poly = get_duwal_poly(row[header])
                    row["Irreducible Poly"] = "$" + poly + "$"
                    row[header] = get_only_id(row[header])

                row_values.append(row[header])
            latex_table += " & ".join(row_values) + " \\\\ \hline \n"

            row_count += 1

        # Generate the LaTeX table footer
        latex_table += "\\end{longtable}"

    return latex_table

# Usage example
csv_file = "duwal_insts.csv"
latex_table = csv_to_latex(csv_file)
print(latex_table)
