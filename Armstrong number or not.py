#Armstrong
n=int(input("Enter a number"))
sod=0
n1=n
while n>0:
    rem=n%10
    sod=sod+rem**3
    n=n//10
if n1==sod:
    print(sod,"is Armstrong")
else:
    print(n1,"is not Armstrong") 


'''
1*1*1+5*5*5+3*3*3=153
3*3*3+7*7*7+0=370
1*1*1+5*5*5+2*2*2=134 not amstrong
'''
