#wap to accept n elem in a list.search an elem  and display its count
l1=eval(input('Enter the number'))
elem=int(input('Enter element to be searched'))
if elem in l1:
    print(l1.count(elem))
else:
    print('Elements no in list')
