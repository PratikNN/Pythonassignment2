#3 write a program to extract all numbers in a file
import re
file = open("a.txt",'r')
for line in file:
    numbers = re.findall('[0-9]+', line)
    print(numbers)
    if not numbers:
        continue
