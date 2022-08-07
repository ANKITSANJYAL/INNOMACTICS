import math
last_min = float(input())
num_students = float(input())
mean = float(input())
sd = float(input())
var = sd**2
mean_prime = num_students * mean
sd_prime = (num_students**(0.5)) * sd
var_prime = num_students * (sd**2)


def cum_pdf(x,mean,var):
    return 0.5*(1 + math.erf( (x-mean)/(2*var)**(0.5) ))
p = cum_pdf(last_min,mean_prime,var_prime)
print(round(p,4))