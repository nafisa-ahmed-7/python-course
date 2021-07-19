'''
Set theory:
a. create a set , b. add members to a set, c. print all elements one by one d. remove an item if present e. union, intersection , difference of 2 sets.
f. Check if one set is subset of another set. g. max, min in set
'''
#a.create a set
user_input =set(input("Enter the elements in the set :").split())
print(user_input)

#b.add members to a set

#c.print all the elements one by one

#d.remove an item if present

x=set(input("Enter the elements in the set 1:").split())
y=set(input("Enter the elements in the set 2 :").split())

#e.union,intersection and difference of two sets
#union
def union_elem(x,y):
    k =set(x.union(y))
    return k
print("Union of two sets:" ,union_elem(x,y))

#intersection
def intersection(x, y):
    l =set(value for value in x if value in y)
    return l
print("Intersection of two sets:" ,intersection(x,y))

#difference of two sets
def difference(x, y):
    m =set(x-y)
    return m
print("Difference of two sets:" ,difference(x,y))

#f.Check one set is subset of another
def issubset(x, y):
    n =(x).issubset(y)
    return n
print("Check if one set is subset of another:" ,issubset(x,y))

#max_min in a set
z=set(input("Enter the elements in the set:").split())
print(z)

def maximum(z):
    return (max(z))
print("The max value of the set is:" ,maximum(z))
def minimum(z):
    return (min(z))
print("The min value of the set is:" ,minimum(z))





