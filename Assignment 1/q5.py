# Print  the leap  years between any two  years. 
# The limit  of the years should  be entered at execution  time.

y1 = int(input('enter year 1 = '))
y2 = int(input('enter year 2 = '))
leap = 0

if (y1%4 == 0 and y1%100 != 0)or(y1%400 == 0):
    leap = 0
else:
    leap = 4 - y1%4
    if((y1+leap) % 100 == 0):
        leap += 4

print('leap years between ', y1, ' and ', y2, ' are : ')

for i in range(y1, y2-leap, 4):
    print(leap+i)