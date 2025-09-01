#Write a program to count number of occurences of word in a string

st=input('Enter string:')
word=input('Enter the word to know its occurence:')
count=0
s=st.split(' ')
print(s)
for i in range(0,len(s)):
    if word==s[i]:
        count+=1
print('No. of times',word,'occurs in the string:',count)        


    
    
