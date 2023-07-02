import csv

def wrap_text_with_eqref(text):
    # Places // between each word in the text
    if text == "---":
        return text
    return "\\eqref{" + text + "}"

def wrap_text_with_shortstack(text):
    if "duwal-13" in text:
        return "\\shortstack{" + text + "}"
    # Places // between each word in the text
    wrapped_text = " \\\\ ".join(text.split())
    return "\\shortstack{" + wrapped_text + "}"

def replace_with_actual_field(text):
    if text == "---":
        return text
    return "$GF(2^" + text + ")$"
def csv_to_latex(csv_file, max_rows):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        headers.pop(headers.index("Why empty?"))
        headers.pop(headers.index("Obs"))

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
            if row_count >= max_rows:
                break

            row["Ref."] = "\\cite{" + row["Ref."] + "}"

            # Wrap text in each cell with \shortstack{}
            for header in headers:
                if header == "Mat." or header == "Inv.":
                    row[header] = wrap_text_with_eqref(row[header])
                #if header == "FF":
                #    row[header] = replace_with_actual_field(row[header])
                if header != "Irreducible Poly":
                    row[header] = wrap_text_with_shortstack(row[header])

            row_values = [row[header] for header in headers]
            latex_table += " & ".join(row_values) + " \\\\ \hline \n"

            row_count += 1

        # Generate the LaTeX table footer
        latex_table += "\\end{longtable}"

    return latex_table

# Usage example
csv_file = "generic_matrices.csv"
max_rows = 10000
latex_table = csv_to_latex(csv_file, max_rows)
print(latex_table)
