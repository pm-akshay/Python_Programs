#wap to print the first occurence of a character in string
st=input('Enter string')
ch=input('Enter the character to be searched:')
pos=1
for i in st:
    if ch==i:
        break
    pos+=1
print('Character',ch,'occured in the position',pos)
