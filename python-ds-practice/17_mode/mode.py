def mode(nums):
    sort = nums.sort()
    counter = 0
    sort_index = sort[0]
    for i in sort:
        curr_frequency = sort.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            sort_index = i
    return sort_index
    

    

    
    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    """Return most-common number in list.