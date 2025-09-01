#wap to print number of words and number of characters present in a string

s=input('Enter string:')
charcount=0
wordcount=1
for i in s:
    charcount+=1
    if i==' ':
        wordcount+=1
print('No.of characters in the string:',charcount)
print('No.of words in the string:',wordcount)        
