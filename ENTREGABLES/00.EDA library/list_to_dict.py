def list_dict(lista):
    dictionary = {}
    for pos, elem in enumerate(lista):
        key = pos
        value = elem
        dictionary[key] = value

    return dictionary
