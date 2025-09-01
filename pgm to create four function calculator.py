#wap to create four function calculator
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
op=input("Choose any one of the operators (+,-,*,/):")
if op=='+':
    result=num1+num2
elif op=='-':
        if num1>num2:
            result=num1-num2
        else:
            result=num2-num1
elif op=='*':
        result=num1*num2
elif op=='/':
        if num2==0:
            print("Error!Division by zero is not allowed")
        else:
            result=num1/num2
else:
     print("Invalid operator")
print("The result is",result)        
         
        
