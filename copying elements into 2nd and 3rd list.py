#accept n elements in a list.Copy all even nums to a 2nd list and odd numbers to a 3rd list
l = eval(input('Enter the elements (as a list): '))
oddlist = []
evenlist = []

for num in l:
    if num % 2 == 0:
        evenlist.append(num)
    else:
        oddlist.append(num)

print('Even numbers:', evenlist)
print('Odd numbers:', oddlist)
        
