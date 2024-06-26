# EXPERIENCE POINTS
# You've been hired by a game studio to work on their latest role-playing game. In this game adventurers need experience points (XP) to level up and become stronger. You've been tasked with creating a function to calculate the total amount of XP needed for a player to reach a specific level.

# Each character starts with 0 XP at level 1. To reach the next level, they need 5 XP more than the last level required. So reaching level 2 requires just 5 XP more, while reaching level 3 requires 10 XP more.

# XP meter

# CHALLENGE
# Complete the calculate_experience_points function.

# The calculate_experience_points function takes a single parameter named level. Determine how many XP are required to get to the specified level from level 1 with 0 XP.

#     #   0xp -> lvl 1 (O * 5)
#     #  +5xp -> lvl 2 (1 * 5)
#     # +10xp -> lvl 3 (2 * 5)
#     # +15xp -> lvl 4 (3 * 5)
#     #------
#     #  30xp

#     calculate_experience_points(4)
#     # returns 30

def calculate_experience_points(level):
    xp_needed = 0
    for i in range(0, level):
        xp_needed += i * 5
    return xp_needed