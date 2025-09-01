#Menu driven program
mylist=[10,20,30,40,50,60,70,80,90,100]
choice=0
while True:
    print('The list "mylist"has the following elemnts',mylist)
    print('\nLIST OPERATIONS')
    print('1.Append an element')
    print('2.Insert an element')
    print('3.Append a list to the given list')
    print('4.Modify an existing element')
    print('5.Delete an exixting element by its position')
    print('6.Exit')
    choice=int(input('ENTER YOUR CHOICE (1-6):'))

    #append an element
    if choice==1:
        element=int(input('Enter the element to be appended:'))
        mylist.append(element)
        print('The element has been appended\n')

    #Insert an element
    elif choice==2:
        element=int(input('The element to be inserted:'))
        pos=int(input('Enter the position'))
        mylist.insert(pos,element)
        print('The element has been inserted\n')

     #Append a list to the given list
    elif choice==3:
        newlist=eval(input('Enter the list to be appended:'))
        mylist.extend(newlist)
        print('The list has been appended\n',newlist)

     #Modify an existing element
    elif choice==4:
         i=int(input('Enter the position of the element to be modified:'))
         if i<len(mylist):
             newelement=int(input('Enter the new element:'))
             oldelement=mylist[i]
             mylist[i]=newelement
             print('The element',oldelement,'has been modified\n')
         else:
             print('Position of the element is more than the length of the list')

      #Delete an exixting element by its position
    elif choice==5:
           i=int(input('Enter the position of the element to pe deleted:'))
           if i<len(mylist):
               element=mylist.pop(i)
               print('The element',element,'has been deleted')
           else:
               print('\nPosition of the element is more than the length of list')

       # Exit from the menu
    elif choice == 6:
        break
    else:
        print('Choice is not valid')
        print('\n\nPress any key to continue.......')
        ch = input()









         
