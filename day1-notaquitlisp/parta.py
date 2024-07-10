def whatfloor(pattern):
    floor=0
    for character in pattern:
        if character == "(":
            floor += 1
        else:
            floor -= 1

    return floor


