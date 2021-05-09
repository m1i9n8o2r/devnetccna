
'''
#Assign to a variable
readdata = open("README.txt", "r")

#.read allows me to read the file
print(readdata.read())

#if using open, need to use close
readdata.close
'''
#Can use "with" and it will close the file for me
with open("README.txt", "r") as data:
    print(data.read())

with open("README.txt", "a+") as data:
    data.write("\nAgregando segunda linea por medio de with open append")

with open("README.txt", "r") as data:
    print(data.read())

