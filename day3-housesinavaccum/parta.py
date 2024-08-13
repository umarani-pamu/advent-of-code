def countuniquehouses(directions):
    current_position=(0,0)  # datatype tuple is mostly used for coordinate pairs
    visited=set()  # used a set instead of list because we dont want duplicate values, as list can have duplicate values
                                            
    visited.add(current_position)  # add() method is used to include new elements into a [set]

    # visted.append(current_position), we cannot use append() method as it appends an element to the end of the [list]

    for movement in directions:
        x, y = current_position
        if movement == "^":
            current_position = (x, y + 1)  
        elif movement == "v":
            current_position = (x, y - 1)  
        elif movement == ">":
            current_position = (x + 1, y) 
        elif movement == "<":
            current_position = (x - 1, y)
        
        visited.add(current_position)
    return len(visited)  
        
        
        
    """ 
        if movements == "^":
            current_position=current_position[0],current_position[1] + 1
        if movements == "v":
            current_position=current_position[0],current_position[1] - 1
        if current_position == ">":
            current_position=current_position[0] + 1,current_position[1]
        if current_position=="<":
            current_position=current_position[0] - 1,current_position[1] 
    
    """

                