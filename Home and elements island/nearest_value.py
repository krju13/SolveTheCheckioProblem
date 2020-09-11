def nearest_value(values:set,one:int)->int:
    li=list(values)
    cha=abs(li[0]-one)
    res=li[0]
    for x in li:
        if cha>abs(x-one):
            cha=abs(x-one)
            res=x
        elif cha==abs(x-one):
            res = x if res>x else res
    return res



print(nearest_value({4,7,10,11,12,17},9))
print(nearest_value({0,-2},-1))


#other person's code that I understood
def nearest_value(values: set, one: int) -> int:
    return min((abs(n-one), n) for n in values)[1]
