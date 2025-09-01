# write a pgm to print the multiplication table of a number of user's choice.
n=int(input("Enter a no:"))
i=1
print("Multiplication table of", n, ":")

while i<11:
    print(i,'*',n,'=',(i*n))
    i+=1
    
    
