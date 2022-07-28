# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
y = int(input())
a,b = divmod(x,y)
print(a,b, (a,b), sep="\n")