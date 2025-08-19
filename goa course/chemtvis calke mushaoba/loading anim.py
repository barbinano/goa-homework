import time
import sys
def loading_screen():

 for i in range(4):  # how many times it repeats
    for dots in range(4):  # "", ".", "..", "..."
        sys.stdout.write("\rLoading" + "." * dots + "   ")  # overwrite line
        sys.stdout.flush()
        time.sleep(0.5)  # delayc
        i=0
        i=i+1
 

import time
import sys

def print_loading():
   for i in range(4):  # how many times it repeats
    for dots in range(4):  # "", ".", "..", "..."
        sys.stdout.write("\rLoading" + "." * dots + "   ")  # overwrite line
        sys.stdout.flush()
        time.sleep(0.5)  # delayc
        if i == 3 and dots == 3:
            sys.stdout.write("\rTransaction Complete! \n")  # overwrite line
            sys.stdout.flush()



