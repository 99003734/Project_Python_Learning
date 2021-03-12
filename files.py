import csv
with open('python.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

import csv
with open('python.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'The Column names are as follows {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

import pandas
df=pandas.read_csv("python.csv")
print(df)

import xlrd
loc = ('workBook1.xlsx')
wb = xlrd.workBook1(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)