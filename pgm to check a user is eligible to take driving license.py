#pgm to check whether a user is eligible to apply for a driving license
name=str(input("Enter the name:"))
age=int(input("Enter the present age:"))
if age>=18:
    print(name,"is elegible")
else:
    print(name,"is not eligible")
