
try:
    from gpiozero import LED
    red = LED(23)
    blue = LED(24)
    green = LED(25)

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
            red.on()
            time.sleep(.5)
        
            red.off()
            green.on()
            time.sleep(.5)
        
            green.off()
            blue.on()
            time.sleep(.5)
            blue.off()

        except:
            pass

alarm(17,9, False )

