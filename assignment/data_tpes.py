# working on lists
l=[1,28,3,7,5,18]
# slicing of a list
print(l[0:4])
# sorting of list
l.sort()
print("sorted list is ",l)
# revrsing of a list
l.reverse()
print("reversed list is ",l)
# appending an element into the list
l.append(8)
print(l)
# inserting an element at a particular position
l.insert(3,6)
print("after inserting 6 at position 3 the list is ",l)
# WORKING on dictionary
# printing the values of a dictionary
mydict={
    "country" : "india",
    "language": "english",
    "marks":100
}
print(mydict.values())
# printing the keys of a dictionary
print(mydict.keys())
# updating the dictionary
mydict.update({"language":"hindi"})
print(mydict)
# Working on sets
# adding elements into a set
set={"lohith",1,2,3,65,448,False}
set.add(8)
print("after adding the set is ",set)
# union of sets
set2={144,"lohith",65,3}
print(set.union(set2))
# intersection of sets
print(set.intersection(set2))