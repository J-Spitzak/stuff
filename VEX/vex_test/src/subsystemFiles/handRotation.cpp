#include "main.h"

//helper
void setClawEffector(int power){
    clawEffector = power;
}

//driver control

void setClawEffectorMotor(){
    int ClawEffectorPower = 127 * (controller.get_digital(pros::E_CONTROLLER_DIGITAL_R1) - controller.get_digital(pros::E_CONTROLLER_DIGITAL_R2));
    setArmRotation(ClawEffectorPower);
}
