
def gale_shapley(A, B):
    pairings = {} 
    unpaired = set(a for a in A.keys()) 
    proposals = {a: 0 for a in A.keys()}
    
    while unpaired:
        a = unpaired.pop()
        ap = A[a] 
        choice = ap[proposals[a]]
        proposals[a] += 1
        if choice in pairings: 
            amatch = pairings[choice]
            bp = B[choice]
            if bp.index(a) < bp.index(amatch):
                pairings[choice] = a
                unpaired.add(amatch) 
            else:
                unpaired.add(a)
        else:
            pairings[choice] = a

    return [(a, b) for (b, a) in pairings.items()]

def test1():
    A = {"Alice": ["Bob", "Bill"],
         "Alyssa": ["Bill", "Bob"]}
    B = {"Bob": ["Alice", "Alyssa"],
         "Bill": ["Alyssa", "Alice"]}
    return gale_shapley(A, B)

def test2():
    A = {"Anna": ["Kristoff", "Olaf"],
         "Elsa": ["Olaf", "Kristoff"]}
    B = {"Kristoff": ["Anna", "Elsa"],
         "Olaf": ["Elsa", "Anna"]}
    return gale_shapley(A, B)
                   
def test_gs():
    A = {"Alice": ["Bob", "Billy", "Brian"],
         "Amy": ["Billy", "Bob", "Brian"],
         "Alyssa": ["Bob", "Brian", "Billy"]}
    B = {"Bob": ["Alice", "Amy", "Alyssa"],
         "Billy": ["Alice", "Amy", "Alyssa"],
         "Brian": ["Alyssa", "Amy", "Alice"]}
    pairings = gale_shapley(A, B)
    # pairings = gale_shapley(B, A)

    return pairings


    
