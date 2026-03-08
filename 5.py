#lists
'''
list=[1,34,"bru",4.6]
print (list)    

list.append("sugar")
print (list)    

list.insert(0,0)
print (list)   

list.pop(4)
print (list)

list[1]="one"
print (list)

list.remove("sugar")
print (list)   

list.clear()
print (list)

list=[1,34,2,4.6,7,8,3]
print(sum(list [0:2]))    #sum of first two elements

list.sort()
 #sort in descending order
print(list)
list.reverse()
print(list)'''

#nested lists
list =[[1,2,3],[4,5,6] ]
list.sort()

print(list[-1])

Nested_list=[[] for n in range(2,6)]
print(Nested_list)