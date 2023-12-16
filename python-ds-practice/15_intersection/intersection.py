def intersection(l1, l2):
    
    lists_int = list(set(l1) & set(l2))

    return lists_int
    
    
    
    
    
    # """Return intersection of two lists as a new list::
    
    #     >>> intersection([1, 2, 3], [2, 3, 4])
    #     [2, 3]
        
    #     >>> intersection([1, 2, 3], [1, 2, 3, 4])
    #     [1, 2, 3]
        
    #     >>> intersection([1, 2, 3], [3, 4])
    #     [3]
        
    #     >>> intersection([1, 2, 3], [4, 5, 6])
    #     []
    """