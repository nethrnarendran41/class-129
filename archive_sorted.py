import csv 
data = []
with open('archive_dataset.csv')as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)
#print(data[0])
headers = data[0]
planet_data = data[1:]
for data in planet_data:
    data[2]= data[2].lower()
planet_data.sort(key = lambda planet_data:planet_data[2])
with open('archive_dataset_sorted.csv','w',newline = '')as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)