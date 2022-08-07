from sklearn import linear_model
# input
i = input().split() 
n = int(i[0])       # number of features    
l = int(i[1])       # number of samples
x=[]
y=[]
for _ in range(l):
    inp = list(map(float,input().split()))
    temp =[]
    for val in range(n):
        temp.append(inp[val])
    x.append(temp)
    y.append(inp[n])

out_len = int(input()) # length of samples for which the prediction is to be made
out_array=[]  
for _ in range(out_len) :
    inp = list(map(float,input().split()))
    out_array.append(inp)

# calculating the coefficient and intercept
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_

# predicting the value for the given samples
for val in out_array:
    b_sum =0
    for i in range(n):
        b_sum += b[i]*val[i]
    y_pred = a + b_sum
    print(round(y_pred,2))