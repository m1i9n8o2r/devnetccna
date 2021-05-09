#Import csv first
import csv

#Read the file into a file handle
samplefile = open("csv_file.csv")

#Create a reader object and run the read function
samplereader = csv.reader(samplefile)

#Can now modify the data
sampledata = list(samplereader)

print(sampledata)

#Now using with instead
with open("csv_file.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]
        print(f'{device} is in {location} and has ip {ip}.')