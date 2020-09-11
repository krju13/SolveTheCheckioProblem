def frequency_sort(items):
    dic={}
    for i in items:
        if dic.get(i)==None:
            dic[i]=items.count(i)
    dic=sorted(dic.items(),reverse=True,key=lambda i:i[1])
    print(dic)
    items=[]
    for key,value in dic:
        while value>0:
            value-=1
            items.append(key)
    return items

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
