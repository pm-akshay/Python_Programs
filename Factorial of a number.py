#Wap to print factorial of a number
n=1
product=1
num=int(input("Enter the no:"))

while n<=num:
    product*=n
    n+=1

print("Factorial of", num,"is",product)
