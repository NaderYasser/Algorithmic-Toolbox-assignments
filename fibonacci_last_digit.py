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
        x = fib[i-1]%10
        y = fib[i-2]%10
        fib.append(x+y)
    return fib[n]%10
    
t= Fibonacci(a)    
print(t)


