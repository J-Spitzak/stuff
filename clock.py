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
    while True:
        print("DONE")
        time.sleep(1)


alarm(8,57, False )

