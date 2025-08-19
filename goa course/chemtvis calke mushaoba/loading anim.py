import time
import sys
for i in range(4):  # how many times it repeats
    for dots in range(4):  # "", ".", "..", "..."
        sys.stdout.write("\rLoading" + "." * dots + "   ")  # overwrite line
        sys.stdout.flush()
        time.sleep(0.5)  # delayc
        i=0
        i=i+1
 


