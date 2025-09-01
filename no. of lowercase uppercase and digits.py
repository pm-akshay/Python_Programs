#WAP to count number of lowercase,uppercase letters,and digits in a string.
s=input('Enter the string:')
uppercount=lowercount=digitcount=others=0
for i in s:
    if i.islower():
        lowercount+=1
    elif i.isupper():
        uppercount+=1
    elif i.isdigit():
        digitcount+=1
    else:
        others+=1
print('No.of lowercase letters:',lowercount)
print('No.of uppercase letters:',uppercount)
print('No. of digits:',digitcount)
print('No.of other charaters:',others)
