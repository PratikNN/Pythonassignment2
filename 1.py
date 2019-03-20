#1 write a program to replace the line which starts with "From:" to "To:" and the line which starts with "To:" should be replaced.
fhand=open("a.txt","w")
s="From:"
s1="To:"
for line in fhand:
     if(line.startswith(s)):
          line.replace(s,s1)
     elif(line.startswith(s1)):
          line.replace(s1,s)

