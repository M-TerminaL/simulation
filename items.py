# ---- items Method ----
# ex: data = {'a': 1, 'b': 2, 'c': 3}
# ex: data.items() --> [('a', 1), ('b', 2), ('c', 3)]
# ----
#------------------------------------------------------
# ---- Functional Way ----

def items(dictionary):
    result = []
    for key in dictionary:
        result = result + [(key, dictionary[key])]
    return result

a = items({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(a)
    
# ---- End Functional Way ----
#------------------------------------------------------







        
