#wap to count the number of times a character occurs in a string
st=input('Enter the string:')
ch=input('Enter the character to be searched:')
count=0
for char in st:
    if char==ch:
        count+=1
print('No. of times',ch,'occurs in the string:',count)        
