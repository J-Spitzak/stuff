red = 23
blue = 24
green = 25

try:
    import RPi.GPIO as io
    io.setup(red, io.OUT)
    io.setup(blue, io.OUT)
    io.setup(green, io.OUT)

except:
    print("does not have IO libraries")

import time



def alarm(Hour, Minute = 0, NxtDay = True, Hr = int(time.strftime("%H", time.localtime())), Min = int(time.strftime("%M", time.localtime()))):

    print(time.strftime("%H:%M:%S", time.localtime()))

    
    #Hr = current time
    #Min = current time
    #Hour = hour of target
    #Minute = minute of target


    if NxtDay != True:
        
        HrLeft = Hour - Hr
    else:
        HrLeft = (24 - Hr) + Hour

    MinLeft = Minute - Min

    if MinLeft < 0:
        HrLeft -= 1
        MinLeft = 60 + MinLeft


    print("time left:", HrLeft, ":", MinLeft)
    

    minutesLeft = MinLeft + HrLeft * 60

    time.sleep(minutesLeft * 60)
    for _ in range(100):
        try:
            print("done")
            io.output(red, io.HIGH)
            time.sleep(.5)
        
            io.output(red, io.LOW)
            io.output(green, io.HIGH)
            time.sleep(.5)
        
            io.output(green, io.LOW)
            io.output(blue, io.HIGH)
            time.sleep(.5)
            io.output(blue, io.LOW)
        except:
            pass

alarm(16,55, False )

