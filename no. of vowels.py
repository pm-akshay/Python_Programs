#Write a program to print number of vowels in a string
n=input('Enter the string:')
vowels='aeiouAEIOU'
vowelcount=0
for i in n:
    if i in vowels:
        vowelcount=vowelcount+1
print('No.of vowels in the string:',vowelcount)        
