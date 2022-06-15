# Find  the prime  numbers  between two given  numbers

n1 = int(input('enter the first number : '))
n2 = int(input('enter the second number : '))

i = n1
prime = []

for i in range(n1, n2):
    count = 0
    for j in range(2, i):
        if i%j == 0:
            count += 1
            break

    if (count == 0) and (i > 2):
        prime.append(i)

print("the prime numbers between ", n1, " and ", n2, " are as follows : ")

for i in range(0, len(prime)):
    print(prime[i])