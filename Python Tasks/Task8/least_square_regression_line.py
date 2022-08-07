x = [95,85,80,70,60]
y = [85,95,70,65,70]
mean_x,mean_y = sum(x)/len(x), sum(y)/len(y)
x_square = 0
xy = 0
for a,b in zip(x,y):
    x_square += a**2
    xy += a*b
n = len(x)
# calculating the slope
b = ( n*xy - sum(x)*sum(y)) / (n*x_square - (sum(x))**2 )

# calculating the intercept
a = mean_y - b*mean_x

y_pred  = a + b* 80
print(round(y_pred,3))