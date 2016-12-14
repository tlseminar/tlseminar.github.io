
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

robotsA = { "Luxo": ["AIBO", "Big Dog", "Junior"],
            "R2-D2": ["AIBO", "Junior", "Big Dog"],
            "Wall-E": ["Big Dog", "Junior", "AIBO"] }
robotsB = { "AIBO": ["Wall-E", "Luxo", "R2-D2"],
            "Big Dog": ["R2-D2", "Luxo", "Wall-E"],
            "Junior": ["Wall-E", "R2-D2", "Luxo"] }
    
    

    
