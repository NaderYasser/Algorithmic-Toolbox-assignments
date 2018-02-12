# Uses python3
# There are two ways of running this program:
# 1. Run
#     python3 APlusB.py
# then enter two numbers and press ctrl-d/ctrl-z
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python3 APlusB.py < dataset.txt
n = int(input())
a = [int(x) for x in input().split()]

index = 1
for i in range(2,n):
    if(a[i]>a[index]):
        index= i
a[n-1], a[index] = a[index], a[n-1]

index = 1
for i in range(2,n-1):
    if(a[i]>a[index]):
        index = i
        
a[n-2],a[index] = a[index],a[n-2]    

print(a[n-2] * a[n-1])
