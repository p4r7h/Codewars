# Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):
# Example: (Input1, Input2 -->Output)

def sum_str(a, b):
    if a is '':
        if b is '':
            return '0'
        else : return b
    elif b is '':
        return a
    else : return str(int(a) + int(b))
pass
