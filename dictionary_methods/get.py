# ---- get Method ----
# ex: data = {'a': 1, 'b': 2, 'c': 3}
# ex: data.get('a', default=None) --> 1
# ----
# ------------------------------------------------------
# ---- Functional Way ----

def get(dictionary, key, default=None):
    value = None
    try:
        value = dictionary[key]
    except:
        if default == None:
            return
        else:
            return default
    return value


a = get({'a': 1, 'b': 2, 'c': 3}, 'b')
b = get({'a': 1, 'b': 2, 'c': 3}, 'u', default='not found')
c = get({'a': 1, 'b': 2, 'c': 3}, 'z')

print(a)
print(b)
print(c)
# ---- End Functional Way ----
# ------------------------------------------------------
