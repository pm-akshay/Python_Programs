#pgm to find the larger of two numbers of users choice
num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
if num1>num2:
    print(num1,">",num2)
if num2>num1:
    print(num2,">",num1)
if num1==num2:
    print(num1,"=",num2)
