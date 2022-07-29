def split_and_join(line):
    # write your code here
    lis = line.split(" ")
    lis = "-".join(lis)
    return lis
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)