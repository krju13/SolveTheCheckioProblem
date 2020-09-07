def backward_string_by_word(text: str) -> str:
    # your code here
    stack=[]
    res=''
    for t in text:
        if t.isspace():
            while len(stack)>0:
                res+=stack.pop()
            res+=' '
        else:
            stack.append(t)
    while len(stack)>0:
        res+=stack.pop()
    return res


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))
    print(backward_string_by_word('world'))
    print(backward_string_by_word('hello   world'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")


#other person's solution
def backward_string_by_word(text: str) -> str:
    return ' '.join([i[::-1] for i in text.split(' ')])
