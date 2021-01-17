#Ex1
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# output:{apple', 'cherry'}
    
#Ex2
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# output:{apple', 'cherry'}

#ex3
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(thisset)
# output:{'banana', 'cherry'}


#ex4
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# output: set()
    