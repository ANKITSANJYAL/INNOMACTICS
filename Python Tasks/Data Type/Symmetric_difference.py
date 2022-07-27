# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
m = set(map(int,input().split()))
input()
n = set(map(int,input().split()))
print(*sorted(m^n), sep="\n")