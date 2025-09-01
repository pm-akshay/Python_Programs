#print prime numbers b/w any two numbers
start=int(input('Enter the 1st number:'))
end=int(input('Enter the 2nd number:'))
print("The prime numbers in the range are:")
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
            
