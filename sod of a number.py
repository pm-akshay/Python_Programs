#wap print sum of digits of a number
n=int(input("Enter the number:"))
sod=0
while n>0:
    rem=n%10
    sod=sod+rem
    n=n//10
print("Sum of the digits is",sod)


