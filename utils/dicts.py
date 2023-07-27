# файл dicts.py
def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    """
    if collection == {}:
        return default
    else:
        return collection[key]