# CONVERTING BINARY
# You've been assigned to write some tests for the Python interpreter itself! Python has built-in functionality to parse strings of 1's and 0's as binary numbers.

# CHALLENGE
# Complete the body_parts function. It takes binary strings as input and returns them in the same order as integers. Each integer is the numerical value of the string when interpreted as binary.

def body_parts(num_heads, num_arms, num_fingers):
    heads = int(num_heads, 2)
    arms = int(num_arms, 2)
    fingers = int(num_fingers, 2)
    return heads, arms, fingers
