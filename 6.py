#tuples
'''t1 = (1, 4, 3, 4, 5)
print(t1)


single_element_tuple = (5)
print(single_element_tuple)

print(t1[-2])#second last element
print(t1.count(1))#count of 1 in the tuple
print(t1.index(4)) #first occurrence of 4

print(1 in t1) #check if 1 is present in the tuple  

t3= (7,8,9)
print(t1 + t3) #concatenation of two tuples 
print(t1 * 2) #repetition of tuple
print(len(t1)) #length of the tuple
'''

#sets
'''s1={1,2,3,4,5,5,4}
print(s1)

print(set()) #empty set  

s2={4,5,6,7,8,"apple","banana"}
print(s1.union(s2)) #union of two sets
us= s1 | s2
print(us)

print(s1.intersection(s2)) #intersection of two sets
inter_s= s1 & s2
print(inter_s)

print(s1.difference(s2)) #difference of two sets
diff_s= s1 - s2
print(diff_s)

print(s1.symmetric_difference(s2)) #symmetric difference of two sets
sym_diff_s= s1 ^ s2 
print(sym_diff_s)

s1.add(6) #adding element to set
print(s1)
s1.remove(3) #removing element from set
print(s1)           
s1.clear() #clearing the set
print(s1)'''

t1= (1,2,3,8)
t2= (4,5,6)

print(t1 + t2) #concatenation of two 
print(t1[2:4])
#t1[2]=10 #tuples are immutable


s1={"apple","banana","cherry "}
s2={"banana","kiwi","orange"}
print(s1.union(s2)) #union of two sets
print(s1.difference(s2)) #difference of two sets
print(s1.intersection(s2)) #intersection of two sets
s1.discard("kiwi") #removing element from set
print(s1)
#s1.remove("kiwi") #removing element from set
print(s1)

l1=[1,2,3,4,5]
t1=tuple(l1)
print(t1)
s1=set(l1)
print(s1)