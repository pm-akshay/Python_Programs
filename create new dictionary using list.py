#Write a program to create a new dictionary using a list which stores the value and
#number of occurrence of the value in the list.
num={}
list1=[2,2,4,5,6,7,8,9,10]
for i in list1:
    val=list1.count(i)
    num[i]=val
print(num)    
    
    
