# PARKING METER
# A parking enforcement officer was assigned to check on some faulty parking meters on Main Street. He determined that the meters were giving tickets to cars whose parking duration had not yet expired.

# CHALLENGE
# The parking agency has tasked you with fixing the code for the meters.

# Create a check_parking_meter function. It takes two inputs:

# time_parked - the amount of time the car has been parked in minutes
# time_purchased - the amount of time the driver purchased on the meter in minutes
# If time_parked meets or exceeds time_purchased return the string "overtime charged"
# Otherwise, return the string "no charges yet"
# Bonus: Try to accomplish this without an "else" statement.

def check_parking_meter(time_parked, time_purchased):
    if time_parked >= time_purchased:
        return 'overtime charged'
    return 'no charges yet'
