f = open("paresh.txt")
f.seek(0)
print(f.tell())

print(f.readline())
print(f.tell())

print(f.readline())
print(f.tell())


f.close()