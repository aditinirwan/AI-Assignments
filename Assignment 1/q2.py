# WAP to create a list  of 100  random  numbers  between 100  and  900.Count  and print  the : 
# (i)All  odd  numbers   (ii)All  even numbers   (iii)All  prime  numbers

from random import randint

i = 0
numbers = []
odd = []
even = []
prime = []

while i < 100:
    i += 1
    x = randint(100, 900)
    numbers.append(x)

    if x%2 == 0:
        even.append(x)
    else:
        odd.append(x)
    
    count = 0
    for j in range(2, x):
        if x%j == 0:
            count += 1
            break
    
    if count == 0:
        prime.append(x)

print("freq of odd number = ", len(odd))
for i in range(0, len(odd)):
    print(odd[i], " ")

print("freq of even number = ", len(even))
for i in range(0, len(even)):
    print(even[i], " ")

print("freq of prime number = ", len(prime))
for i in range(0, len(prime)):
    print(prime[i], " ")
