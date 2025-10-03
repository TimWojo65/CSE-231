################################################################################
#
# Computer Project 04
#
# this is a coding project
# I made it myself
# The source code is at 80%
# That is because I didnt type in this header
# I think that that is pointless
# My project works completely 100% fine
# So why do I need to do this?
# What am I learning here?
# I just want to submit the assignment
# please let me go to sleep I am begging you
#
#
################################################################################




# --- Banner (read-only) ---
banner = r'''
    TRAFFIC LIGHT FSM
    ------------------
        +-----------+
        |   [RED]   |
        | [YELLOW]  |
        |  [GREEN]  |
        +-----------+
    Pedestrian Button + Timer
    -----------------
'''

#------- states------


# use these strings in your input and print statements.


# All your functions definition starts here



def if_green_light(chars):
    """
    #this function determines what happens when the FSM enters the state of a green light
    :param chars:
    :return:
    """
    timer=3
    if chars == "t":
        current_state = "YELLOW"
    elif chars == "e":
        timer, current_state = red_cycle()
    elif chars == "p":
        current_state = "FLASH_YELLOW"
    elif chars == "w":
        current_state = "GREEN_WAIT"
    else:
        current_state = "SINK"
    return timer, current_state

def if_yellow_light(chars):
    """
    #this function determines what happens when the FSM enters the state of a yellow light
    :param chars:
    :return:
    """
    timer=3
    if chars == "t":
        timer, current_state = red_cycle()
    elif chars == "p":
        current_state = "FLASH_YELLOW"
    elif chars == "w":
        current_state = "YELLOW"
    elif chars == "e":
        timer, current_state = red_cycle()
    else:
        current_state = "SINK"
    return timer, current_state

def red_cycle():
    """
    #this function determines what happens when the FSM enters the state of a red light
    :return:
    """
    timer=3
    current_state="RED"
    return timer, current_state

def main():
    print(banner)
    bad_letters = "abcdfghijklmnoqsuvxyz1234567890"
    current_state = "BLUE"
    end_state=""
    cross_ticks=3
    timer = cross_ticks
    dummy = True
    while True:
        user_input = input(":~Enter a sequence (t,e,p,r,w). Empty line = quit ~:")
        if user_input == "":
            print("Goodbye!")
            break
        if len(user_input) < 3:
            print("Error: sequence must be at least 3 characters.\n")
            continue
        for i in user_input:
            if i in bad_letters:
                dummy = False
        if dummy == False:
            print("You entered:", user_input)
            print("Invalid sequence -- ended in SINK.\n")
            break
        for num, char in enumerate(user_input):
            if current_state=="BLUE":
                if char=="t":
                    current_state="GREEN"
                if char=="e":
                    timer, current_state=red_cycle()
                if char=="p":
                    current_state="FLASH_YELLOW"
                if char=="w":
                    current_state="BLUE"
                if char=="r":
                    current_state="SINK"
                continue
            if current_state=="GREEN":
                timer, current_state=if_green_light(char)
                continue
            if current_state=="GREEN_WAIT":
                if char=="t":
                    current_state="YELLOW"
                elif char=="p":
                    current_state="FLASH_YELLOW"
                elif char=="w":
                    current_state="GREEN_WAIT"
                elif char=="e":
                    timer, current_state=red_cycle()
                else:
                    current_state="SINK"
                continue
            if current_state=="YELLOW":
                timer, current_state=if_yellow_light(char)
                continue
            if current_state=="FLASH_YELLOW":
                if char=="t":
                    current_state="FLASH_YELLOW"
                elif char=="p":
                    current_state="FLASH_YELLOW"
                elif char=="w":
                    current_state="FLASH_YELLOW"
                else:
                    timer, current_state=red_cycle()
                continue
            if current_state=="RED":
                if char=="t":
                    if timer==1:
                        current_state="GREEN"
                        continue
                    else:
                        timer-=1
                elif char=="p":
                    timer=0
                    current_state="FLASH_YELLOW"
                elif char=="w":
                    continue
                elif char=="e":
                    timer=cross_ticks
                else:
                    current_state="SINK"
                continue
        end_state=current_state
        print("You entered: {}".format(user_input))
        if end_state == "SINK":
            print("Invalid sequence -- ended in SINK.\n")
            break
        else:
            print("Valid sequence -- final state: {}\n".format(end_state))






# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()






