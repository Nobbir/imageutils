import filecmp

from PIL import Image
from PIL.ExifTags import TAGS
import sys
import os
from PIL import ImageChops
from PIL import Image
from PIL import ImageStat
import hashlib

# this long value
# or the concatenated string value
# could be used as Hash 

def convertDateToLong(date_str):
    
    dt = date_str.split()[0]
    tm = date_str.split()[1]
    year, month, day = dt.split(":")
    year = int(year.strip())
    month = int(month.strip())
    day = int(day.strip())

    hour, minute, second = tm.split(":")
    hour = int(hour.strip())
    minute = int(minute.strip())
    second = int(second.strip())

    return second * 1 + minute * 100 + hour * 10000 + day * 1000000 + month * 100000000 + year * 10000000000

    
def convertDateToYMDHMS(date_str): # 2010:07:14 20:43:00

    dt = date_str.split()[0]
    tm = date_str.split()[1]
    year, month, day = dt.split(":")
    year = int(year.strip())
    month = int(month.strip())
    day = int(day.strip())

    hour, minute, second = tm.split(":")
    hour = int(hour.strip())
    minute = int(minute.strip())
    second = int(second.strip())

    return year, month, day, hour, minute, second


def compare_dates(date1, date2):

    # we can use just logical operators 
    # on date objects, e.g., date1 == date2
    dt1 = format_date_str(date1)
    dt2 = format_date_str(date2)

    diffs = []
    for i in range(6):
        diffs.append(abs(dt1[i] - dt2[i]))
        
    return diffs

if __name__ == "__main__":
    d1 = convertDateToLong('2010:07:15 20:43:00')
    d2 = convertDateToLong('2010:07:14 20:43:01')
    d3 = convertDateToLong('2010:09:15 20:43:55')
    d4 = convertDateToLong('2011:07:14 20:53:01')
    d5 = convertDateToLong('2007:01:20 08:43:55')
    d6 = convertDateToLong('2015:05:10 12:13:21')

    if d1 > d2:
        print("Bigger")
    else:
        print("Smaller or equal")