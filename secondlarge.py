list1 = [10,20,5,1,62,54]

#assuming max_ is equal to maximum of element at 0th and 1st index and secondmax is the minimum among them
max_=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
for i in range(2,len(list1)):
   # if found element is greater than max_
   if list1[i]>max_:
      secondmax=max_
      max_=list1[i]
   #if found element is greator than secondmax
   else:
      if list1[i]>secondmax:
         secondmax=list1[i]
print("Second highest number is the list is : ",str(secondmax))
