# Write a pgm to print whether a number is palindrome or not
n=int(input("Enter no:"))
rev=0
n1=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if n1==rev:
    print(rev,"is a palindrome")
else:
    print("not a palindrome")
