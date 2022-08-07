f = open("paresh2.txt","w")
#f = open("paresh2.txt","a")


"""#f.write ("my job place is Pune\n")
a = f.write ("My job place is Pune\n")
print(a)
f.close()"""


f = open("paresh.txt","r+")

#f.write ("My native place is Akkalkot\n")
print(f.read())
f.write("my name is paresh\n")

f.close()