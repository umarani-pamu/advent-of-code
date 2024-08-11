    
def calculate_ribbon(length, width, height):
    volume =length * width * height 
    perimeter1=2*(length + width)
    perimeter2=2*(width + height)
    perimeter3=2*(height + length)
    smallest_side_perimeter = min(perimeter1,perimeter2,perimeter3)
    return volume + smallest_side_perimeter
    
