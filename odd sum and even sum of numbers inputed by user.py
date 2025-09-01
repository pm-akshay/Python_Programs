#pgm to find odd sum and even sum of numbers inputed by the user
n=int(input("Enter the limit:"))
ctr=1
evensum=oddsum=0
while ctr<=n:
    num=int(input('num'))
    if num%2==0:
        evensum=evensum+num
    else:
        oddsum=oddsum+num
    ctr+=1
print('The sum of even  numbers:',evensum)
print('The sum of odd  numbers:',oddsum)
