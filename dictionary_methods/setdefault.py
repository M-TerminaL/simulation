# ---- setdefault Method ----
# ex: data = {'a': 1, 'b': 2, 'c': 3}
# ex: data.setdefault('a') --> 1
# ex: data.setdefault('d', 4) --> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ex: data.setdefault('b', 6) --> {'a': 1, 'b': 2, 'c': 3}
# ----
#------------------------------------------------------
# ---- Functional Way ----

def setdefault(dictionary, key, default=None):
    if key not in dictionary and default is not None:
        dictionary[key] = default
        return dictionary
    if key not in dictionary and default == None:
        return f'key : "{key}" not found'
    for k in dictionary:
        if k == key:
            return dictionary[key]
        

a = setdefault({'a': 1, 'b': 2, 'c': 3}, 'b')
b = setdefault({'a': 1, 'b': 2, 'c': 3}, 'b', 12)
c = setdefault({'a': 1, 'b': 2, 'c': 3}, 'd', 4)
d = setdefault({'a': 1, 'b': 2, 'c': 3}, 'z')

print(a)
print(b)
print(c)
print(d)

# ---- End Functional Way ----
#------------------------------------------------------







        
