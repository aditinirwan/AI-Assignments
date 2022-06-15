# D is a dictionary  defined as D= {1:”One”, 2:”Two”, 3:”Three”, 4: “Four”, 5:”Five”}.
# (i)WAP to add new entry in D; key=6 and value is “Six”
# (ii)WAP to  remove key=2.
# (iii)WAP to  check if  6 key  is  present in  D.
# (iv)WAP to  count  the number  of elements  present in  D.
# (v)WAP to  add all  the values  presentinD.

Dict = { 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five" }
print("Dictionary = ", Dict)

# (i)) adding new entry
Dict[6] = "Six"
print("Dictionary = ", Dict)

# (ii) removing entry 2
Dict.pop(2)
print("Dictionary = ", Dict)

# (iii) to check if 6 is present in Dict
if 6 in Dict:
    print("yes key 6 is present in Dict")
else:
    print("No it is not present")

# (iv)) to count the number of elements in Dict
print("number of elements in Dict = ", len(Dict))

# (v) to add all values present in d
sum = 0
for i in Dict.keys():
    sum = sum + i

print("Sum of all elements in the dictionary is ", sum)