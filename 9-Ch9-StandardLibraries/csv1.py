import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["product_id", "id", "price"])
    writer.writerow(["1", "2", "10"])
    writer.writerow(["80", "13", "101"])


with open("data.csv") as file:
    reader = csv.reader(file)
    for read in reader:
        print(read)
