#SLICING

list1=[10,20,30,40,50,60,70,80,90,100]

#10,20,30....100
print(list1[::1])  #or (list1[0:10])

#10,20,30,40
print(list1[0:4])

#20,40,60,80
print(list1[1:8:2])

#60,70,80
print(list1[5:8])

#-ve slicing
#100,90,80,....10
print(list1[::-1])

#90,70,50,30
print(list1[-2:-9:-2])

#50,60,70,80
print(list1[-6:-2])


