def print_formatted(n):
    # your code goes here
    binn = bin(n).replace("0b","")
    for i in range(1,n+1):
        deci = str(i)
        deci = (len(binn)-len(deci))*" "+deci
        
        octa = oct(i).replace("0o","")
        octa = (len(binn)-len(octa))*" "+octa
        
        hexi = hex(i).replace("0x","").upper()
        hexi = (len(binn)-len(hexi))*" "+hexi
        
        bina = bin(i).replace("0b","")
        bina = (len(binn)-len(bina))*" "+bina
        print(deci,octa,hexi,bina)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)