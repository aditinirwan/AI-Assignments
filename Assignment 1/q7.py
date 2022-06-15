# Write  a Python  program  to  check the validity  of password  input  byusers. Validation: 
# At least 1 letter  between [a-z] and 1 letter  between [A-Z]. 
# At least 1 number  between [0-9]. 
# At least 1 character from  [$#@]. 
# Minimum  length  6 characters. 
# Maximum  length  16  characters

password = input('enter password : ')

flag = 0
lower = 0
upper = 0
number = 0
spChar = 0


if len(password) < 17 and len(password) > 5:
    flag = 1

if flag == 1:
    for i in range(0, len(password)):
        if ord(password[i]) > 64 and ord(password[i]) < 91:
            upper += 1
        elif ord(password[i]) > 96 and ord(password[i]) < 123:
            lower += 1
        elif ord(password[i]) > 47 and ord(password[i]) < 58:
            number += 1
        elif ord(password[i]) == 35 or ord(password[i]) == 36 or ord(password[i]) == 64:
            spChar += 1

if flag and upper and lower and number and spChar:
    print("Valid password! ")
else:
    print("Invalid password! ")