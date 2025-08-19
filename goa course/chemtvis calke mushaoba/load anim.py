import time            # Gives us time.sleep() to pause between frames
import sys             # Lets us write to stdout without automatic newline

for i in range(10):    # Repeat the whole animation 10 times
    for dots in range(4):                         # 0,1,2,3  → "", ".", "..", "..."
        sys.stdout.write("\rLoading" + "." * dots + "   ")
        # \r = carriage return → move cursor to start of the SAME line
        # "." * dots builds the dot string
        # trailing "   " overwrites leftover characters from the previous frame
                               
        time.sleep(0.5)             