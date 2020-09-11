def split_list(items: list) -> list:
    n = len(items)
    first,second=[],[]
    if(n==0):return [first,second]
    elif(n==1):return[items,second]
    else:
        n-=1
        first=items[0:int(n/2)+1]
        second=items[int(n/2)+1:]
        return [first,second]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
