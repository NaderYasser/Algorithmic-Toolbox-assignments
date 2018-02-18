# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt

a = int(input())

def Fibonacci(n):
  if(n <= 1):
    return n 
  else:
    fib=[0,1]
    
    for i in range(2,n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
    
x= Fibonacci(a)    
print(x)


