#Methods in a list
list1=[1,2,3,4,5,6,7,8]

#len
print(len(list1))          #len is used to print the length of the list.

#list()
print(list1)

#append
list1.append('[10,20,30]') 
print(list1)               #append is used for inserting a single element in the end of the list.

#extend
list1=[1,2,3,4,5,6,7,8]
list1.extend([9,10])  
print(list1)               #extend adds more than one element to the end of the list

#insert
list1.insert(0,9)
print(list1)               #inserts an element at a particular index in the list.

#count
list1=[1,2,3,4,5,6,7,8]
print(list1.count(1))      #count returns the number of times a given element appears in the list.

#remove
list1=[1,2,3,4,5,6,7,8]
list1.remove(1)
print(list1)               #Remove the given elements from the list.

#pop
list1=[1,2,3,4,5,6,7,8]
print(list1.pop(5))        #pop removes an item at the specified index from the list.

#index
list1=[1,2,3,4,5,6,7,8]
print(list1.index(5))      #index method helps you find the index position of an element.If element is not present,value error is generted.

#reverse
list1=[1,2,3,4,5,6,7,8]
list1.reverse()
print(list1)               #Reverses the order of elements in a given list.

#sort
list1=[1,4,2,3,5,9,8,7,6]
list1.sort()
print(list1)               #sorts the elements of a given list in-place

#sorted
list1=[4,2,3,1,6,5,7,8]
list2=sorted(list1)
print(list1)
print(list2)               #takes a list and returns a new list with those elements in sorted order

#Max
list1=[1,2,3,4,5,6,7,8]
print(list1) 
print(max(list1))          #it returns largest element from the list

#Min
list1=[1,2,3,4,5,6,7,8]
print(list1)
print(min(list1))          #it returns the smallest element from the list

#sum
list1=[1,2,3,4,5,6,7,8]
print(sum(list1))          #it returns the sum of the elements in the list



