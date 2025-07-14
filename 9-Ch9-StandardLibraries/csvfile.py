import csv

# with open("csvfile.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["col1", "col2", "col3"])
#     writer.writerow([1, "col2Value", 20.4])
#     writer.writerow([2, "col2Value1", 20.3])


with open("csvfile.csv") as file:
    reader = csv.reader(file)
    print(type(reader))
    print(reader.line_num)
    # print(list(reader))
    for row in reader:
        print(row)
    
