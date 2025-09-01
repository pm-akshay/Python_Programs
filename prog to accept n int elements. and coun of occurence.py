#Write a program to accept n integer elements in a list. Search for an element and
#display the count of its occurrence
n=int(input('Enter the limit:'))
newlist=[]
for i in range(n):
    elem=int(input('Enter element'))
    newlist.append(elem)
print(newlist)
chk=int(input('Enter the elements to be checked'))
if chk in newlist:
    print(newlist.count(chk))
else:
    print('Number not in list')
