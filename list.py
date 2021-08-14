# ---- Introduction ----

# Lists are used to store multiple items in a single variable.

# Example:

myName = "dibwe"
my_age = 144
my_address = "144 west ave, ferndale, Randburg"

my_details = [myName, my_age, my_address]

this_is_a_list = ["school", "stundent", "car", "people"]

# print(my_details)

#   ----Access : How can it be accessed  ? ----

#   List items are ordered, changeable, and allow duplicate values.

#   List items are indexed, the first item has index [0], the second item has index [1] etc.

# print("-- Printing my details ---")
# my_summary = my_details[0] + " is a student, his age: " + \
#     str(my_details[1]) + " years old"
# print(my_summary)

# print("-- original printing details---")
# print(my_details)

# print("-- original printing updated details---")

# my_updated_details = [my_details[0] + " Kalangu ", my_details[1:]]
# my_details[0] = "Dibwe Kalangu"
# my_details[2] = "355 west avenue Ferndale"
# print([my_details[0], my_details[2]])

#   ----  Change : How can we update data within the data type ? ----

#   The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#   Update / change list Item

# print("---- edid 1 items ---")
# this_is_a_list[0] = "shool"
# print(this_is_a_list)

# print("---- edid 3 items ---")
# this_is_a_list[0:3] = ["clip-school", "me", "toyota"]
#my_details = [myName, my_age, my_address]

my_details[1:3] = [149, "243 afganistan"]
# print(my_details)

# print(this_is_a_list)


#  Add    : How can we add items to the data structure ?

# print("--- append 1 element ---")
# this_is_a_list.append("earth")
# print(this_is_a_list)

my_details.append(True)
# print(my_details)

#   Remove : How can we remove items to the data structure?
# print("--- Remove one item from the list ---")
# this_is_a_list.remove("earth")
# print(this_is_a_list)

#del my_details[-1]

# print(my_details)
# using index

# print("--- Removing the first item ---")
# this_is_a_list.pop(0)

# print("--- Done removing one item ---")


#   Loop   : How can we loop throught the data structure ?

# print("--- looping through items ---")

# for item in this_is_a_list:
#     print(item)


# for detail in my_details:
#     if type(detail) != str:
#         print(detail)


#   Sort   : can we sort it ?
#['dibwe', 149, '243 afganistan', True]
my_details_copy = []
for detail in my_details:

    if type(detail) != str:
        my_details_copy.append(str(detail))
    else:
        my_details_copy.append(detail)

# my_details_copy.append(True)
# this_is_a_list.sort()
# for item in my_details_copy:
#     if type(item) != str:
#         print("a non str was found")
#         break
#     else:
#         print("all good")

my_details_copy[2:].sort(reverse=True)
# print(my_details_copy)

# print("--- looping through items ---")

# for item in this_is_a_list:
#     print(item)

#   Copy   : can we copy it ?

my_details_copy_two = my_details.copy()
#   Join   :  How do we join it to similar ones?
my_details_cop_three = my_details_copy + my_details_copy_two
# print(my_details_cop_three)

#   List   : What method does the data structure provide?
