#  for loop 
# there is function ius range function in for loop. 
# the range () function in the python is used to genrated a sqence  number 




# for i range (strat,stop, stp up ) this a snatx to wriet code 
for i  in range (0,8,2):
  print (i)




# #  for loop with else 
# an optional else can be used with a loop if the code is to be executed when  loops exhurts 

l=[1,6,6,7]
for item in l :
    print (item)
else:
 print("this is done")
 


#  break statment  
# Break is used to come out from thw loop from encoutered . it insttructure the program to exit  the loop now 
 for i in range (  0 , 100):
   print(i)
   if(i==3):
      break
print(" this is end the loop ")
#     


#  continue satement  in for loop 
#   continue statment is use for skipe the value when is ist wronhg value that skip and procied the code fprqward 
for i in range (  0 , 100):
   print(i)
   if(i==3):
      continue 
print(" this is end the loop ")
#     