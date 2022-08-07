f = open("Paresh.txt" )

#print(f.readlines())    # It will print a string output
#rint(f.readline())
#print(f.readline())  # This is a another type of function we can use to read file line by line
#content = f.read()
#print(content)

"""content = f.read(3)
print(content)

content = f.read(3)
print(content)

content = f.read(753)
print(content)"""

"""for line in content:   #It is read charter by charter
    print(line)"""

for line in f:   #It is read line  by line
    print(line ,end="")
f.close()