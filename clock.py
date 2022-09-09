import time


# now = datetime.now()

# print(now.strftime("%H:%M:%S"))
def alarm(Hour, Minute):

    while True:
        now = time.localtime()
        print(time.strftime("%H:%M:%S", now))




