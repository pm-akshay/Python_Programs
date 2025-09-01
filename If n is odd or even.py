#Pgm to assign 5 int in a tuple.If n is odd display 3n+1 else display n/2
t1=(2,3,4,5,6)
for n in t1:
    if n%2!=0:
        print(n,'is odd: 3n+1',(3*n)+1)
    else:
        print(n,'is even: n/2',n//2)

