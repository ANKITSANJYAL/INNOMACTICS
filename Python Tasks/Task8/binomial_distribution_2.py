# input
values = list(map(float, input().split()))
p = (values[0] / 100)
n = int(values[1])

def fact(n):
    if n == 1 or n==0:
        return 1
    fact = 1
    for val in range(1,n+1):
        fact *= val
    return fact

def binom(x,n,p):
    f =  fact(n)/(fact(n-x)*fact(x))
    return f * (p**x ) * (1-p)**(n-x)

# no more than 2 rejects means we have to consider {0,1,2} rejects
nm = 0 
for i in range(3):
    nm += binom(i,n,p)
print(round(nm,3))
# atleast 2 rejects means { 2,3,4,5,6,7,8,9,10}
at = 0 
for i in range(2,11):
    at += binom(i,n,p)
print(round(at,3))
    