# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
count = 0
value = 0

for i in range(int(input())):
    if A.issuperset(set(input().split())):
        count += 1
    else:
        value += 1
if value != 0:
    print('False')
else:
    print('True')