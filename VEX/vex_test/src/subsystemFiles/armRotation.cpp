#include "main.h"

//HELPER FUNCTION:

void setArmRotation(int power){
    armRotation = power;
}

//DRIVER CONTROL FUNCTIONS

void setArmRotationMotor(){
    int ArmRotationPower = 127 * (controller.get_digital(pros::E_CONTROLLER_DIGITAL_L1) - controller.get_digital(pros::E_CONTROLLER_DIGITAL_L2));
    setArmRotation(ArmRotationPower);
}