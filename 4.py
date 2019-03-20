#4.write a program to read a file line by line write the file each line in areverse order to another file

f = open("a.txt", "rb")
s = f.read()
f.close()
f = open("c.txt", "wb")
f.write(s[::-1])
f.close()