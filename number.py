def number(range=[]):
    try:
        x = int(input("Enter a number: "))
        if(bool(range)):
            if((x>range[0]-1)and (x< range[1]+1)): return x
            else: return
        else:
            return x
    except:
        raise Exception('Number not an integer!')
