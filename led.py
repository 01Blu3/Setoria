#include all necessary packages to get LEDs to work with Raspberry Pi
import datetime, time, board, neopixel

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
# we are using the D.21  since we have the leds connected to GPIO port 21
pixels1 = neopixel.NeoPixel(board.D21, 60, brightness=1)

#Also create an arbitrary count variable
int_time = 0
x=1
state = "ok"

# creates a variable keeping track of time


#Focusing on a particular strip, use the command Fill to make it all a single colour
#based on decimal code R, G, B. Number can be anything from 255 - 0. Use an RGB Colour
#Code Chart Website to quickly identify the desired fill colour.
pixels1.fill((0, 128, 0))

# Breathing effect and status indicator
# Green means the agent is in good condition, yellow means neutral condition agent should be prerparing to leave, red means agent should be pulled as soon as possible

def fill_range(rgb_val_1, rgb_val_2, rgb_val_3, inc_1, inc_2, inc_3, dec, last):
    if dec:
        for num in range(15):
            rgb_val_1-= inc_1
            rgb_val_2-= inc_2
            rgb_val_3+= inc_3

            pixels1.fill((rgb_val_1, rgb_val_2, rgb_val_3))
            time.sleep(0.08)

    if last:
        for num in range(15):
            rgb_val_1-= inc_1
            rgb_val_2+= inc_2
            rgb_val_3+= inc_3

            pixels1.fill((rgb_val_1, rgb_val_2, rgb_val_3))
            time.sleep(0.08)

            
    for num in range(15):
        rgb_val_1-= inc_1
        rgb_val_2+= inc_2
        rgb_val_3+= inc_3

        pixels1.fill((rgb_val_1, rgb_val_2, rgb_val_3))
        time.sleep(0.08)
    


while x:
    # Checks how long the agent has been out
    if int_time > 60 and int_time < 120:
        state = "neutral"
    elif int_time > 120:
        state = "danger"


    if state == "ok":
        fill_range(0,114,0, 0, 2, 0, False, False)
        int_time+=1.6


    if state == "neutral":
        fill_range(255, 255, 0, 2, 2, 1, True, False)
        int_time+=1.6
        

    if state == "danger":
        fill_range(255,0,0, 3, 0, 1, False, True)
        int_time+=1.6
    
    

    # pixels1[x] = (255, 0, 0)
    # pixels1[x-5] = (255, 0, 100)
    # pixels1[x-10] = (0, 0, 255)
    #Add 1 to the counter
    x=x+1
    # #Add a small time pause which will translate to 'smoothly' changing colour
    # time.sleep(0.05)


