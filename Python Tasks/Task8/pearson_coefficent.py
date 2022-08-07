import statistics
size = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))
mean_x,mean_y = statistics.mean(x) , statistics.mean(y)
sd_x,sd_y = statistics.pstdev(x),statistics.pstdev(y)
num =0
for a,b in zip(x,y):
    num += (a-mean_x)*(b-mean_y)
pcc = num/(size*sd_x*sd_y)
print(round(pcc,3))