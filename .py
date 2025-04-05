# creating a list 

my_list=[1, 2, 3, 4, 5]
print(my_list)
 #append a new element to the list
# since append() method can only take one argument, we need to append each element separately.
my_list.append(10) 
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#Output: [1, 2, 3, 4, 5, 10, 20, 30, 40]

#insert a new element at a specific position in the list
my_list.insert(2,15)
print(my_list)
#Output: [1, 2, 15, 3, 4, 5, 10, 20, 30, 40]

#extend the list by appending elements from another list
my_list.extend([50, 60, 70])
print(my_list)
#Output: [1, 2, 15, 3, 4, 5, 10, 20, 30, 40, 50, 60, 70]

#remove last element from the list
my_list.pop()
print(my_list)