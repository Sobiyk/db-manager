def convert_to_tuple(key, object):
    key = [int(key)]
    if isinstance(object, list):
        key.extend(object)
        return key
    elif isinstance(object, dict):
        key.extend(list(object.values()))
        return key
    elif isinstance(object, (int, str, float)):
        key.append(object)
        return key
