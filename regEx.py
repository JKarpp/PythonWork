import re

text = input("Enter a Sting to see the number of vowles:    ") 
lower = text.lower()
regX = re.findall("(a|e|i|o|u)", lower)
a = 0
e = 0
i = 0
o = 0
u = 0
for x in regX:
    
    if x == "a":
        a = a+1
    if x == "e":
        e = e+1
    if x == "i":
        i = i+1
    if x == "o":
        o = o+1
    if x == "u":
        u = u+1
print(f"The Number of a's is {a}, \nThe Number of e's is {e}")
print(f"The Number of i's is {i}, \nThe Number of o's is {o}")
print(f"The Number of u's is {u}")
