# Enter your code here. Read input from STDIN. Print output to STDOUT
#take rows and columns and convert both to integer using map function 
rows,columns = map(int,input().split())
#Middle row where "WELCOME" will be written
middle = rows//2+1
#Top part of door mat
for i in range(1,middle):
    #calculate number of .|. required and multiply with .|.
    center = (i*2-1)*".|."
    #Move our center pattern to center using string.center method and fill left and part with "-" 
    print(center.center(columns,"-"))
#print middle part welcome
print("WELCOME".center(columns,"-"))
#create bottom part in reverse order like we did in the top part
for i in reversed(range(1,middle)):
    center = (i*2-1)*".|."
    print(center.center(columns,"-"))