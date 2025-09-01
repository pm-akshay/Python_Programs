#Write a program to perform four functions of a calculator.
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
add=a+b
print('The sum is',a+b)
if a>b:
    print('The difference is',a-b)
else:
    print('The difference is',b-a)
mult=a*b
div=a/b
print('The mul is',a*b)
print('The div is',a/b)
