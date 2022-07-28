# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b,c = (int(input()) for i in range(3))
print(pow(a,b), pow(a,b,c), sep="\n")