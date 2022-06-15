# (i)  Write  a function  which  takes principal  amount,  interest  rate and  time.  
# This  function returns compound  interest. Call  this  function  to print  the output.

def cmpINT(pr,rt,time):
    amt = 0
    amt = pr*pow(1 + rt/100, time)
    return amt