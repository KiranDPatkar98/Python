def add(a, b):
    try:
        return int(a)+int(b)
    except ValueError as err:
        return err
