
def sort(s):
    r = {}
    ks = [key for key in s]
    ks.sort(key=str.lower)
    for k in ks:
        r.setdefault(k, s.get(k))
    return r