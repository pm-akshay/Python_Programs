#Write a program to accept the name and age of n persons. Display names of those
#who are eligible to vote
n=int(input("Enter number of persons"))
d1={}
for i in range(n):
    nm=input("Enter name")
    age=eval(input("Enter age"))
    d1[nm]=age
print(d1)
for ky in d1:
    if d1[ky]>=18:
     print(ky,"can vote")
