# Find  the common  elements  from  two lists.

a = [1,2,3,4,5,6,7,8,9,10]
b = [5,10,6,11,7,12,8,13,9,14,]
common = []

for i in range(0, len(b)):
    for j in range(0, len(a)):
        if a[j] == b[i]:
            common.append(b[i])
            continue

print("List A : ")

for i in range(0, len(a)):
    print(a[i])

print("List B : ")

for i in range(0, len(b)):
    print(b[i])

print("common elements in list A and B are : ")

for i in range(0, len(common)):
    print(common[i])