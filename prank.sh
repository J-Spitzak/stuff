#!/bin/bash

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# this is an april fools prank that is run from the terminal, just run it from the terminal
# it looks just like a real terminal (you will have to change the username) but whenever anything
# is typed in it just says command not found and prints april fools with the command tree 
# a few things to note:
# 1.
#   control c or quitting the terminal will end the program
# 2. 
#   in a real terminal if the command kjfi eurg was entered it would return command not found kjfi
#   this is because even if the command can't be found it treats eurg as an argument, my program does not
# 3.
#   my cover story:
#   my cover story for my target (Jeff Elkner, my cs teacher) is that this has happened before and 
#   quitting it stopped it but I want to experiment with it more so he should not quit the session
#   also that there was one command that worked (tree) but I won't remember it until a minute in
#if anybody actually uses this other than me I would love to see it
#please record and send a video to jason.spitzak@gmail.com
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

clear

while :
do

    read -p "1002864@1002864-student-FVFG349LQ6L3 ~ % " INPUT 


    if [[ $INPUT == 'tree' ]]
    then
        echo APRIL FOOLS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else
        echo zsh: command not found: $INPUT
    fi


done