import math
max_wt = float(input())
num_boxes = float(input())
mean = float(input())
sd = float(input())
var = sd**2
mean_prime = num_boxes * mean
sd_prime = (num_boxes**(0.5)) * sd
var_prime = num_boxes * (sd**2)


def cum_pdf(x,mean,var):
    return 0.5*(1 + math.erf( (x-mean)/(2*var)**(0.5) ))
p = cum_pdf(max_wt,mean_prime,var_prime)
print(round(p,4))