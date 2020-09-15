from functools import cmp_to_key
def comp(a,b):
    if a[1]>b[1]:return -1
    elif a[1]==b[1]:
        if a[0]<b[0]:return -1
        else: return 1
    else:return 1


def frequency_sorting(numbers):
    numbers=sorted(numbers)
    frequen=[]
    for n in range(101):
        frequen.append([n,0])
    for x in numbers:
        frequen[x][1]+=1
    frequen=sorted(frequen,key=cmp_to_key(comp))
    numbers=[]
    for x in frequen:
        for n in range(x[1]):
            numbers.append(x[0])
    return numbers

if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5,3,3,3,2,2,5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
