#Accept age of 5 students and remove those elements with age<20
age=(12,20,24,25,22)
agelist=list(age)
for i in agelist:
    if i<20:
        agelist.remove(i)
new_agelist=tuple(agelist)
print(new_agelist)

        
