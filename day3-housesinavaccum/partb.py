def roboversion(directions):
    santa_position=(0,0)
    robosanta_position=(0,0)
    visited=set()  
    visited.add(santa_position)
    
    for index,direction in enumerate(directions):
        if index%2==0:
            santa_position=movement(santa_position,direction)
            visited.add(santa_position)
        else:
            robosanta_position=movement(robosanta_position,direction)
            visited.add(robosanta_position)
        
    return len(visited)     
        
        
def movement(position,direction):
    x, y = position
    if direction == "^":
        position = (x, y + 1)  
    if direction == "v":
        position = (x, y - 1)  
    if direction  == ">":
        position = (x + 1, y) 
    if direction  == "<":
        position = (x - 1, y)
    return position    
        
    
        
        

                