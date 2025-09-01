#Create a tuple to store n alphabets and display all the elements in the tuple except’d’
n=5
t1=('a','c','d','f','g')[:n]# Select first n alphabets from the given sequence
print('Original tuple:',t1)
for i in t1:
    if i!='d':
        print(i)
