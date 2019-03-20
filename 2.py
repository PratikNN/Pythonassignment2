#2 write a program to read through a text file and print the contents of the text file in upper case.
fhand=open("a.txt")
for line in fhand:
    a=line.upper()
    print(a)

