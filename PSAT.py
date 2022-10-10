import time
input("press enter to start")
start = time.time()
timeLeft = 60*25
tpq = timeLeft/17
last_elaps = 0
for _ in range(17):
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
print("you finished in", thisTime, "seconds, the time neccesary was", 60*25)
if thisTime > 60*25:
    print("you were too slow by", thisTime - 60*25)
else :
    print("you were", 60*25 - thisTime, "seconds ahead of time")
