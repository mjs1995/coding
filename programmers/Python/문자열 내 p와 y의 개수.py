from collections import Counter

def solutions(s):
    a = Counter(s.lower())
    if a['p'] == a['y']:
        return True
    else:
        return False
solutions(s)
