def sayposition(pattern):
    floor=0
    for position,character in enumerate(pattern,start=1):
        if character == "(":
            floor += 1

        elif character == ")":
            floor -= 1
        
        if floor == -1 :
            return position

    return -1

