

import copy

list= [1,2,3,5,6,7,8,104,111,1001]
list_copy = copy.deepcopy(list)
list2=[]


for number in list_copy:
  if number % 2 != 0:
    list.remove(number)

print(list)