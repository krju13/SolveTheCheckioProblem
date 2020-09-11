def removesame(sub):
    a=' '
    for n in sub:
        if n!=a[-1]:
            a+=n
    return a
def check_help(sub):
    return True if sub.find("help")>-1 else False

def check_asap(sub):
    return True if sub.find("asap")>-1 else False

def check_urgent(sub):
    return True if sub.find("urgent")>-1 else False

def is_stressful(subj):
    if subj[-3:] =="!!!":
        return True
    if subj.isupper():
        return True
    subj=''.join([i for i in subj.lower() if i.isalpha()])
    subj=removesame(subj).lstrip()
    return check_help(subj)|check_asap(subj)|check_urgent(subj)





print(is_stressful("HI"))
print(is_stressful("H-E-l-p"))
print(is_stressful("aaaaasapppp"))
print(is_stressful("haelep u"))
print(is_stressful("where are?!!!"))


if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("H-E-l-p") == True, "3"
    assert is_stressful("aaaaasapppp") == True, "4"
    assert is_stressful("haelep u") == False, "5"
    assert is_stressful("where are you?!!!") == True, "6"
    print('Done! Go Check it!')
