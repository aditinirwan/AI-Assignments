# Write a Python Program to input basic salary of an employee and calculate its Gross salary 
# according to following: 
# Basic Salary <= 10000 : HRA = 20%, DA = 80% 
# Basic Salary <= 20000 : HRA = 25%, DA = 90% 
# Basic Salary > 20000: HRA = 30%, DA = 95%

s = int(input('enter salary '))

if s < 10000:
    da = 0.8*s
    hra = 0.2*s
elif s < 20000:
    da = 0.9*s
    hra = 0.25*s
else:
    da = 0.95*s
    hra = 0.3*s

print('gross salary is ', s + da + hra)