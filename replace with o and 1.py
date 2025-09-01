#accept n elements in a list. Search an element and replace all occurrence of that element with 0 and the rest with 1.
list1=eval(input("Enter elements:"))
elem=int(input("Enter element to be searched and replaced:"))
for i in range(len(list1)):
    if list1[i]==elem:
        list1[i]=0
    else:
        list1[i]=1
print("Modified list:", list1)    
