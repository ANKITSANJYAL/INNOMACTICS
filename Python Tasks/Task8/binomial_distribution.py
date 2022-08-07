l = list(map(float,input().split()))
b = l[0]
g = l[1]
p_boy = b/(b+g)
p_girl = 1 - (b/(b+g))
#print(b,g)
n= 6 # total number of children
boys = 3 # at least 3 boys
p =(p_boy**3)*(p_girl**3)*20 + (p_boy**4)*(p_girl**2)*15 +(p_boy**5)*(p_girl**1)*6 + (p_boy**6)
print(round(p,3))