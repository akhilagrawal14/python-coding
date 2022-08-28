import time

# code to put at start and end to calulate code time between that

start = time.process_time()
# your code here    
print(f"Code exceution time : {time.process_time() - start}")


# code to convert time in diffrent format srtftime
import datetime
datetime.now().strftime('%Y-%m-%d %H:%M:%S')
datetime.now().strftime("%H:%M:%S") # for only time

#timestamp  1st January 1970 at UTC as 0, counting seconds
date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)

#reverse
now = datetime.now()
timestamp = datetime.timestamp(now)
print("timestamp =", timestamp)


#get current date and time
import datetime
now = datetime.datetime.now() # its format datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)


