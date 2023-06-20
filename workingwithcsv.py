#CSV FILES
# using open() works but is better to import csv module
#importing csv module allows us to use the .reader() method to help us read the csv file
import csv

# 'with' allows us to open and close a file without explicitly having to close it
# open(filename, mode) method takes two arguments
# if mode is omitted, opens as r (read) by default
#we then iterate over the rows

with open('data/file1.csv', 'r') as file: #open in reading mode
    readerobject = csv.reader(file) #csv.reader() is used to read the file, which returns an iterable reader object
    for row in readerobject: #reader object is iterated using a for loop to print the contents of each row
        print(row)

imported_data = open('data/file2.csv', 'r')
readerobject2 = csv.reader(imported_data)
x = list(readerobject2)
print(x)
imported_data.close()


with open('data/file3.csv') as file3:
    read_content = file3.read()
    print(read_content)

# DIFFERENT DELIMITERS
# Default is comma
# To change to delimiter is tab,
# reader = csv.reader(file, delimiter = "\t")