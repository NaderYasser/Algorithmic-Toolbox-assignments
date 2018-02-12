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
product = 0
for i in range(n):
    for j in range(i + 1, n):
        product = max(product, a[i] * a[j])
print(product)
