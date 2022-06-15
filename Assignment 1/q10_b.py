# (ii)  Save this  function(as a module)  in  a python  file  and call  it  in  another  python  file.

from q10_a import cmpINT

Principal = int(input("enter Principal Amount : "))
Rate = int(input("enter rate of Interest : "))
Time = int(input("enter time : "))

print("your compund interest is ", cmpINT(Principal, Rate, Time))