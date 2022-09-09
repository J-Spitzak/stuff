import time



def alarm(Hour, Minute = 0):

    now = time.localtime()
    print(time.strftime("%H:%M:%S", now))
    Hr = int(time.strftime("%H", now))
    Min = int(time.strftime("%M", now))

    HrLeft = Hour - Hr
    MinLeft = Minute - Min
    print("time left:", HrLeft, ":", MinLeft)
    minutesLeft = MinLeft + HrLeft * 60
    time.sleep(minutesLeft * 60)
    while True:
        print("DONE")
        time.sleep(1)


alarm(18,59)

