#OPEN FILE
file1 = open("data/textfile.txt","r")
#READ THE FILE
file_content = file1.read()
print(file_content)
#MUST CLOSE FILE
file1.close()
#OR

#USE WITH OPEN as it closes the file after automatically, even if there is an exception
with open("data/textfile.txt","r") as file:
    read_content = file.read()
    print(read_content)

#writing to a file
#If we try to write to file that doesn't exist, new file is created
#If a file already exists, its content is erased and new content added to file
with open("data/textfile2.txt","w") as file2:
    file2.write("Hello world\n")
    file2.write("So long, and thanks for all the fish")

#.readlines() returns the lines as a list
with open("data/songlyrics.txt","r") as file:
    print(file.readlines())

#target a specific line:
with open("data/songlyrics.txt","r") as file:
    print(file.readlines()[6])
    
