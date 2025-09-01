#wap to print prime nos between any two numbers
start=int(input('Enter the lowest value range:'))
end=int(input('Enter the largest value range:'))
print('The prime nos in the range are:')
for number in range(start,end+1):
    if number>1:
        for i in range(2,number):
            if(number%i)==0:
                break
        else:
            print(number)
