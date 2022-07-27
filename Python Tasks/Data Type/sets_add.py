# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

printable_set = set([])

for i in range(n):
    printable_set.add(input())

print(len(printable_set))