import math
sample_size = float(input())
mean = float(input())
sd = float(input())
per_cover = float(input())
z = float(input())

a = mean - z * (sd / math.sqrt(sample_size))
b = mean + z * (sd / math.sqrt(sample_size))

print (round(a,2))
print (round(b,2))