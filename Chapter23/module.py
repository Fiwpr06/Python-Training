def sum_tree(L):
    total = 0
    for x in L:
        if not isinstance(x, list):
            total += x
        else:
            total += sum_tree(x)  
    return total