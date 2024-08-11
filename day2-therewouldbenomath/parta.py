    
def calculate_wrapping(length, width, height):
    surfaceArea = 2 * length * width + 2 * width * height + 2 * height * length
    smallest_side = min(length * width, width * height, height * length)
    return surfaceArea + smallest_side

"""def sum_of_all_wrap(presents):
    totalwrappings = 0
    for present in presents:
        length, width, height = present
        totalwrappings += calculate_wrapping(length, width, height)
    return totalwrappings"""
