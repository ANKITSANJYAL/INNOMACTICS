import math
# input
nd = list(input().split(" "))
mean = float(nd[0])
var  = float(nd[1])**2
more_than = int(input())
less_than = int(input()) 


def cum_pdf(x,mean,var):
    return 0.5*(1 + math.erf( (x-mean)/(2*var)**(0.5) ))

p1 = cum_pdf(more_than,mean,var)
p1 = 1-p1
p2 = cum_pdf(less_than,mean,var) 
p2 = 1-p2
p3 = cum_pdf(less_than,mean,var) 
print(round(p1*100,2))
print(round(p2*100,2))
print(round(p3*100,2))