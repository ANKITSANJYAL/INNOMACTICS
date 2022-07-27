# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
set_a = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation = input().split()
    new_set = set(map(int, input().split()))
    eval('set_a.{}({})'.format(operation[0], new_set))

print(sum(set_a))