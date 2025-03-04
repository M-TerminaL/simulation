# ---- key Method ----
# ex: data = {'a': 1, 'b': 2, 'c': 3}
# ex: data.keys() --> ['a', 'b', 'c']
# ----
# ------------------------------------------------------
# ---- Functional Way ----

def keys(dictionary):
    lst = []
    for key in dictionary:
        lst = lst + [key]
    return lst


a = keys({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(a)

# ---- End Functional Way ----
# ------------------------------------------------------
