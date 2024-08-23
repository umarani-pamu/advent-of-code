import re
def nicestring(string):
    vowels = re.findall(r'[aeiou]', string)
    if len(vowels) < 3:
        return "naughty"

    if not re.search(r'(.)\1', string):
        return "naughty"

    if re.search(r'(ab|cd|pq|xy)', string):
        return "naughty"
    return "nice string"

def count_nicestring(strings):
    count_nice = 0
    for s in strings:
        if nicestring(s) == "nice string":
            count_nice += 1
    return count_nice

"""import re
from collections import Counter
def nicestring(string):
    vowels=re.search(r"[aeiou]",string)
    countVowels=Counter(vowels)
    for count in countVowels.values():
        if countVowels>=3:
            return "Nice string"
        else:
            return "naughty"
    repeated_letter=re.findall(r"[a-zA-Z]",string)
    countRepeat=Counter(repeated_letter)
    for counterr in countRepeat.values():
        return "Nice string"
    pattern=r"(ab|cd|pq|xy)"
    pattern_let=re.search(pattern,string)
    if pattern_let ==True:
        return "Nice String"
    else:
        return "naughty"
string=input()
print(nicestring(string))    
"""

"""
import re
from collections import Counter

def nicestring(string):
    # Find all vowels in the string
    vowels = re.findall(r"[aeiou]", string)
    countVowels = len(vowels)
    
    # Check if there are at least 3 vowels
    if countVowels < 3:
        return "naughty"
    
    # Find all letters in the string
    repeated_letter = re.findall(r"[a-zA-Z]", string)
    countRepeat = Counter(repeated_letter)
    
    # Check if there is at least one letter that appears more than once
    if any(count >= 2 for count in countRepeat.values()):
        return "Nice string"
    
    # Check if the string contains any of the forbidden substrings
    pattern = r"(ab|cd|pq|xy)"
    if re.search(pattern, string):
        return "naughty"
    
    return "Nice string"

# Input and output
string = input()
print(nicestring(string))
"""
