def isEmpty(v):
    return v is None or (type(v) is str and len(v) == 0) or (type(v) is list and len(v) == 0)


def isAnyEmpty(l: list):
    for v in l:
        if isEmpty(v): return True
    return False
