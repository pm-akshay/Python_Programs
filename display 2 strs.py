#WAP to accept two strings and display larger string.
#without using built-in fns
str1=input('Enter string 1:')
str2=input('Enter string 2:')
count1=count2=0
for i in str1:
    count1+=1
for j in str2:
    count2+=1
if count1==count2:
    print('Both are equal')
elif count1>count2:
    print('Larger string is',str1)
else:
    print('Larger string is',str2)
