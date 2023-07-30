#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

try:
    from gpiozero import LED
    red = LED(23)
    blue = LED(24)
    green = LED(25)

except:
    print("does not have IO libraries")

import time

Dude = False






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

    return minutesLeft





class Sub_dude(Node):
    def __init__(self):
        super().__init__("sub_dude")
        self.c = 1


        time.sleep(alarm(17,9, False ) * 60)




        self.msg_subsciber = self.create_subscription(String, "/chatter", self.msg_callback, 10)


        print("done")
        self.timer = self.create_timer(0.5, self.change_color)



    def change_color(self):
        if self.c == 1:
            blue.off()
            red.on()
            self.c += 1
        elif self.c == 2:
            red.off()
            green.on()
            self.c += 1
        elif self.c == 3:
            green.off()
            blue.on()
            self.c == 1



    def msg_callback(self, msg: String):
        red.off()
        blue.off()
        green.off()
        quit()


def main(args=None):
    rclpy.init(args=args)

    node = Sub_dude()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

