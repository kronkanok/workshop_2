#EX1
thisdict ={"brand": "Ford", "model": "Mustang",'year': 1964}
thisdict.pop["model"]
print(thisdict) #output: {'brand': 'Ford','year': 1964}

#ex2
thisdict ={"brand": "Ford", "model": "Mustang",'year': 1964}
thisdict.popitem["model"]
print(thisdict)  #output: {'brand': 'Ford', 'model': 'Mustang'}

#ex3
thisdict ={"brand": "Ford", "model": "Mustang",'year': 1964}
del thisdict["model"]
print(thisdict) #output: {'brand': 'Ford','year': 1964}

#ex4
thisdict ={"brand": "Ford", "model": "Mustang",'year': 1964}
thisdict.clear["model"]
print(thisdict) #output: {}