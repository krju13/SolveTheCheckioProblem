def date_time(time: str) -> str:
    time=time.split()
    time=time[0].split(".")+time[1].split(":")
    def month(num):
        if num=='01':return "January"
        elif num=='02':return "February"
        elif num=='03':return "March"
        elif num=='04':return "April"
        elif num=='05':return"May"
        elif num=='06':return "June"
        elif num=='07':return "July"
        elif num=='08':return "August"
        elif num=='09':return "September"
        elif num=='10':return "October"
        elif num=='11':return "November"
        elif num=='12':return "December"
    res = str(int(time[0]))+" "+month(time[1])+" "+time[2]+" year "
    if(time[3]=='01'):
        res+=str(int(time[3]))+" hour "
    else:
        res+=str(int(time[3]))+" hours "
    if(time[4]=='01'):
        res+=str(int(time[4]))+" minute"
    else:
        res+=str(int(time[4]))+" minutes"
    return res

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
