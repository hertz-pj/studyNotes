def colname_to_num(colname):
    if type(colname) is not str:
        return colname

    col = 0
    power = 1


    for i in range(len(colname)-1,-1,-1):
        ch = colname[i]

        col += (ord(ch)-ord('A')+1)*power

        power *= 26

    return col-1

def trans(str_):
    
    t = 0
    # 26进制
    for i in range(len(str_)):
        t *= 26
        t += ord(str_[i])-ord('A') + 1

    return t-1

if __name__ == "__main__":
    print(colname_to_num("A"))
    print(trans("A"))
    pass