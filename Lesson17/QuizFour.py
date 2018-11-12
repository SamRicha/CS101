# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def download_time(fileSize, fileUnit, downloadSize, downloadFileUnit):
    hours = 0
    minutes = 0
    pluralHours = "hours"
    pluralMinutes = "minutes"
    pluralSeconds = "seconds"
    
    fileSize = fileExtensionFinder(fileSize,fileUnit)
    downloadSize = fileExtensionFinder(downloadSize,downloadFileUnit)
    
    seconds = float(fileSize) / float(downloadSize)
    
    if seconds / 3600 > 0:
        hours = int(seconds) / 3600
        seconds = seconds % 3600
    if seconds / 60 > 0:
        minutes = int(seconds) / 60
        seconds = seconds % 60
    if seconds % 1 > 0 and seconds != 1:
        seconds = round(seconds,10)
    if hours == 1:
        pluralHours = pluralHours[0:4]
    if minutes == 1:
        pluralMinutes = pluralMinutes[0:6]
    if seconds == 1:
        pluralSeconds = pluralSeconds[0:6]
        
    return str(hours) + " " + pluralHours + ", " + str(minutes) + " " + pluralMinutes + ", " + str(seconds) + " " + pluralSeconds
    
def fileExtensionFinder(size,sizeName):
    if sizeName == "kb":
        size *= (2 ** 10)
    elif sizeName == "kB":
        size *= (2 ** 10 * 8)
    elif sizeName == "Mb":
        size *= (2 ** 20)
    elif sizeName == "MB":
        size *= (2 ** 20 * 8)
    elif sizeName == "Gb":
        size *= (2 ** 30)
    elif sizeName == "GB":
        size *= (2 ** 30 * 8)
    elif sizeName == "Tb":
        size *= (2 ** 40)
    elif sizeName == "TB":
        size *= (2 ** 40 * 8)
    return size
    

print download_time(11,'GB', 5, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


