# Find  the sum  of the series (1+x+x2/2!+. . . +xn/n!)

def series():
    n=int(input("Enter n: "))
    x=int(input("Enter x: "))
    fac=1
    sum=1
    pro=1
    for i in range(1,n):
        for j in range(1,i):
            fac=fac*i
        pro=x**n
        sum=sum+(pro/fac)
    print(sum)

series()
