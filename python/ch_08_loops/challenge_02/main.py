# SQUARING NUMBERS
# John is finishing some math homework and needs to calculate the square of some numbers. However, he's getting tired of entering each of them into a calculator individually.

# The square of a number is just the number multiplied by itself.

# CHALLENGE
# In the calculate_squares function, write a loop that calculates and prints the squares of the numbers from the start parameter up to the given end parameter.

# Use the following format to print each line:

# NUM squared = SQUARE
# Copy icon
# Where NUM is the number, and SQUARE is its square.

# For example, the first iteration of the loop in calculate_squares(100, 110) should print:

# 100 squared = 10000
# Copy icon
# Note: The end is exclusive and should not be included in the printed output. This means if start is 10 and end is 12, we only want to print 10 and 11.

def calculate_squares(start, end):
    for i in range(start, end):
        print(f'{i} squared = {i ** 2}')

# Don't edit below this line

def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Calculating squares from {start} to {end - 1}")
    calculate_squares(start, end)
    print("=====================================")


def main():
    test(100, 105)
    test(1, 3)
    test(11, 14)


main()