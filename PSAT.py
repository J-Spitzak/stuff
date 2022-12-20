import time
timeLeft = 60*int(input("total time in minutes:"))
totalMin = timeLeft / 60
totalQ = int(input("total questions"))
tpq = timeLeft/totalQ
last_elaps = 0
input("press enter to start")
start = time.time()
for _ in range(totalQ):
    input()
    elps_frm_strt = time.time() - start
    diff = elps_frm_strt - last_elaps
    if diff > tpq:
        print("uh oh, you were", diff - tpq, "too slow")
    elif diff == tpq:
        print("right on time")

    else:
        print("good job, you were", tpq - diff, "seconds fsater than neccesary")
    last_elaps = elps_frm_strt
print("done")
thisTime = time.time() - start
print("you finished in", thisTime, "seconds, the time neccesary was", 60*totalMin)
if thisTime > 60*totalMin:
    print("you were too slow by", thisTime - 60*totalMin)
else :
    print("you were", 60*totalMin - thisTime, "seconds ahead of time")
