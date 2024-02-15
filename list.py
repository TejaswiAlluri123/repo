#Basic List Operations
#length
List = [1,2,3,4,5]
# if len(List) > 5:
#     print(len(List))
# Output : 5

#Concatenation
List2 = [6,7,8,9,10]
# print(List + List2)
# output : [1, 2, 3, 4,5, 6, 7, 8, 9, 10]

#Repetition
# print(List*3)
# output :[1, 2, 3, 4,5, 1, 2, 3, 4,5, 1, 2, 3, 4,5]

#Membership
#print( 3 in List)
# Output:True

#Iteration

# for i in List:
#     print(i)
# output:1
# 2
# 3
# 4
# 5

#Indexing, Slicing, and Matrixes:
#Offsets start at zero
# print(List[0])
# Output : 1

#Negative: count from the right (starts form -1)
#print(List[-1])
# output : 5

#Slicing fetches sections 
#print(List[2:]) # from element at 2nd index to last element
# Output : [3, 4, 5]

#Built-in List Functions & Methods
# cmp(list1, list2)
# print(len(List)) ---- 5
#print(max(List)) ---- 5
#print(min(List)) -----1

# 	list(seq)
# tuple = (10,8,6)
#List3 = list(tuple)   
#print(List3)
# print(list(tuple))
# Output : [10, 8, 6]

#list.append(obj)
# List.append(100)
# print(List)
# Output : [1, 2, 3, 4, 5]

#returns count of object in the list(how many times the object in list)
#list.count(obj)
# print(List.count(5))
# Output : 1

#list.extend(seq)
# List.extend(List2)
# print(List)
# output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#list.index(obj)   Returns the lowest index in list that obj appears
# List3 = [1,2,1,2,3,4]
# print(List.index(2))
# Output:1

#list.insert(index, obj)  Inserts object obj into list at offset index
# List.insert(2,200)
# print(List)
# Output : [1, 2, 200, 3, 4, 5]

#list.pop(obj=list[-1]) Removes and returns last object or obj from list
# List.pop(-1)
# print(List)
# output : [1, 2, 3, 4] -- delete last object

#list.remove(obj)
# List.remove(2)
# print(List)
# Output : [1, 3, 4, 5]

#list.sort([func])
# L = [100, 300, 200, 500, 400]
# L.sort()
# print(L)
# Output : [100, 200, 300, 400, 500]

#Copy--- L1 = L.copy()






