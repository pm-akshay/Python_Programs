#Pgm to find prime numbers b/w 25 and 30
for num in range(25,31):
    for i in range(2,num):
        if(num%i)==0:
            break
    else:
        print(num)
