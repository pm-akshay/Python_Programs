#wap to print the numbers from 1 to 20.pgm should not print no.divisible by 5
#continue statement
a=0
while(a<20):
    a+=1
    if a%5==0:
        continue
    print(a)
