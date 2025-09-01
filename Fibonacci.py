# write a pgm to print Fibonacci number
term=int(input("Enter no:"))
f=0
s=1
print(f,s,sep=' ')
ctr=3
while ctr<=term:
    t=f+s
    print(t)
    f=s
    s=t
    ctr+=1             

