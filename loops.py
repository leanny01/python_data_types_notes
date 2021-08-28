list = [1,3,4,5,7,89]

# Foor loop

# for number in list:
#     if(number % 2 == 0):
#         continue
#     print(number)
     
# for number in list:
#     if(number % 2 == 0):
#         continue
#     print(number)

n = 0
while(n < len(list)-1):
  n = n + 1
  #print(list[n])
  if(list[n] % 2 != 0):
    continue
   
  print(list[n])
  
# print the sum
# print("The sum is", sum) 
