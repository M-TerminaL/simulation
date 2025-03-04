# ---- pop Method ----
# ex: data = {'a': 1, 'b': 2, 'c': 3}
# ex: data.pop('a') --> {'b': 2, 'c': 3}
# ----
# ------------------------------------------------------
# ---- Functional Way ----

def pop(dictionary, key):
    try:
        del dictionary[key]
    except:
        return f'key "{key}" not found'
    return dictionary


a = pop({'a': 1, 'b': 2, 'c': 3}, 'b')
b = pop({'b': 1, 'b': 2, 'c': 3}, 'z')

print(a)
print(b)

# ---- End Functional Way ----
# ------------------------------------------------------
