# --- Class Dict ---

class DictModifier:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __repr__(self):
        return str(self.dictionary)

    def keys(self):
        result = []
        for key in self.dictionary:
            result = result + [key]
        return result

    def values(self):
        result = []
        for key in self.dictionary:
            result = result + [self.dictionary[key]]
        return result

    def get(self, key, default=None):
        result = 'Not Found'
        try:
            result = self.dictionary[key]
        except:
            if default is None:
                return result
            else:
                result = default
                return result
        return result

    def items(self):
        result = []
        for key in self.dictionary:
            result = result + [(key, self.dictionary[key])]
        return result

    def pop(self, key):
        try:
            value = self.dictionary[key]
            del self.dictionary[key]
        except:
            value = f'key: " {key} " not found.'
        return value

    def setdefault(self, key, default=None):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            self.dictionary[key] = default
