# Create a List  L having  dataas= [10,  20,  30,  40,  50,  60,  70,  80].
# (i)WAP to  add 200  and  300  to L. 
# (ii)WAP to  remove 10  and 30  from  L.
# (iii)WAP to  sort L in  ascending  order.
# (iv)WAP to  sort L in  descending  order.

list = [10, 20, 30, 40, 50, 60, 70, 80]

print("original list : ")
for i in range(0, len(list)):
    print(list[i])

# (i) adding 200 and 300 to list
list.append(200)
list.append(300)

print("after adding 200 and 300 to the list : ")
for i in range(0, len(list)):
    print(list[i])

# (ii) removing 10 and 30 from ist
list.pop(0)
list.pop(1)

print("after removing 10 and 30 from the list : ")
for i in range(0, len(list)):
    print(list[i])

# (iii) sorting in ascending order
list.sort()

print("sorting list in ascending order : ")
for i in range(0, len(list)):
    print(list[i])

# (iv)) sorting in descending order
list.sort(reverse=True)

print("sorting list in descending order : ")
for i in range(0, len(list)):
    print(list[i])