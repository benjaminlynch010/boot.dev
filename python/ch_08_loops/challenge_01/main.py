# ROCKET LAUNCH
# A team of scientists is getting ready to launch the rockets they have been working on. You've been asked to write a program that will countdown to the rockets' launch.

# CHALLENGE
# In the countdown_to_blastoff function, write a loop that counts down from 10 to 1. At each iteration, print the number with an ellipsis:

# i...

# However, when i is 1, it should print 1...Blastoff! instead.

def countdown_to_blastoff():
    for i in range(10, 0, -1):
        print(f'{i}...')
    print('Blastoff!')

# Don't edit below this line

def test():
    print("Counting down to blastoff:")
    countdown_to_blastoff()
    print("=====================================")


def main():
    test()


main()
