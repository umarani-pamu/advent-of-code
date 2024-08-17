import hashlib

def find_adventcoin(secretkey):
    number = 0
    while True:
        input_string = f"{secretkey}{number}"
        result = hashlib.md5(input_string.encode()).hexdigest()
        if result.startswith("00000"):
            return number
        number += 1
