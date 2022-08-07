import math
# input
nd = list(input().split(" "))
mean = float(nd[0])
var  = float(nd[1])**2
less_than = float(input())
range_ = list(input().split(" "))
from_val = float(range_[0])
to_val   = float(range_[1])


def cum_pdf(x,mean,var):
    return 0.5*(1 + math.erf( (x-mean)/(2*var)**(0.5) ))


# less than 19.5 hours

p1 = cum_pdf(less_than,mean,var)

# between 20 and 22

p2 = cum_pdf(to_val,mean,var) - cum_pdf(from_val,mean,var) 
print(round(p1,3))
print(round(p2,3))