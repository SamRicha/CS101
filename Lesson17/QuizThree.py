# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(seconds):
    hours = 0
    minutes = 0
    pluralHours = "hours"
    pluralMinutes = "minutes"
    pluralSeconds = "seconds"
    
    if seconds / 3600 > 0:
        hours = int(seconds) / 3600
        seconds = seconds % 3600
    if seconds / 60 > 0:
        minutes = int(seconds) / 60
        seconds = seconds % 60
    if seconds % 1 > 0 and seconds != 1:
        seconds = round(seconds,1)
    if hours == 1:
        pluralHours = pluralHours[0:4]
    if minutes == 1:
        pluralMinutes = pluralMinutes[0:6]
    if seconds == 1:
        pluralSeconds = pluralSeconds[0:6]
        
    return str(hours) + " " + pluralHours + ", " + str(minutes) + " " + pluralMinutes + ", " + str(seconds) + " " + pluralSeconds
        
print convert_seconds(1)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
