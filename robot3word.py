#the robot distinguish 3 word in succession

def checkio(words: str) -> bool:
    words=words.split()
    num=0
    for n in words:
        if num>=3:
            return True
        if n.isdecimal():
            num=0
        else: num+=1
    if num>=3:
        return True
    return False
def checkiobetter(words):
    num=0
    for n in words.split():
        if n.isalpha()==True:
            num+=1
            if num==3:return True
        else: num=0
    return False
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
