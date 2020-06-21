import csv

file_to_read = "Tasks/Lesson4/orderdata_sample.csv"
file_to_write = "Tasks/Lesson4/new_file.csv"

read_file = open(file_to_read, "r", newline="")
write_file = open(file_to_write, "w", newline="")

reader = csv.reader(read_file)
writer = csv.writer(write_file)

skip_first_row_read = next(reader)

data = [["Total"]]

for row in reader:
    total = float(row[3]) * float(row[4]) + float(row[5])
    data.append([total])

writer.writerows(data)