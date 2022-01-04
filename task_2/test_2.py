import datetime
import spiceypy
import numpy as np


spiceypy.furnsh("task_2/meta_2.txt")

INIT_TIME_UTC = datetime.datetime(year=2000, month=1, day=1, hour=0, minute=0, second=0)

DELTA_DAYS = 10000
END_TIME_UTC = INIT_TIME_UTC + datetime.timedelta(days=DELTA_DAYS)

INIT_TIME_UTC_STR = INIT_TIME_UTC.strftime("%Y-%m-%dT%H:%M:%S")
END_TIME_UTC_STR = END_TIME_UTC.strftime("%Y-%m-%dT%H:%M:%S")

print("Init time in UTC: %s" % INIT_TIME_UTC_STR)
print("End time in UTC: %s\n" % END_TIME_UTC_STR)

INIT_TIME_ET = spiceypy.utc2et(INIT_TIME_UTC_STR)
END_TIME_ET = spiceypy.utc2et(END_TIME_UTC_STR)

print("Init time in ET: %s" % INIT_TIME_ET)
print("End time in ET: %s\n" % END_TIME_ET)
