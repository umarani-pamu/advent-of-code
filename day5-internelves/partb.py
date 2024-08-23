import re
def new_nicestring(string):
    if not re.search(r'([a-zA-Z]{2}).*\1', string):
        return "naughty"

    if not re.search(r'([a-zA-Z]).\1', string):
        return "naughty"
    return "nice string"

def count_new_nicestring(strings):
    count_nice = 0
    for s in strings:
        if new_nicestring(s) == "nice string":
            count_nice += 1
    return count_nice
