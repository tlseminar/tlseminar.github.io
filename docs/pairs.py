
##
## cs2102 - Class 16 and 17
##
## Making Lists from functions
##

def make_pair(a, b):
    def selector(which):
        if which:
            return a
        else:
            return b
    return selector

def pair_first(p):
    return p(True)

def pair_last(p):
    return p(False)

def list_prepend(e, l):
    return make_pair(e, l)

def list_first(l):
    return pair_first(l)

def list_rest(l):
    return pair_last(l)

def list_empty(l):
    return l == None

def list_length(l):
    if list_empty(l):
        return 0
    else:
        return 1 + list_length(list_rest(l))

def list_concat(p, q):
    if list_empty(p):
        return q
    else:
        return list_prepend(list_first(p), list_concat(list_rest(p), q))
    
def list_last(l):
    if list_empty(list_rest(l)):
        return list_first(l)
    else:
        return list_last(list_rest(l))

    
def list_reverse(l):
    if list_empty(l):
        return None
    else:
        return list_postpend(list_reverse(list_rest(l)), list_first(l))


list123 = list_prepend(1, list_prepend(2, list_prepend(3, None)))

    
