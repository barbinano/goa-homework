import time
import sys

try:
    while True:
        for dots in range(4):
            sys.stdout.write("\rProcessing" + "." * dots + "   ")
            sys.stdout.flush()
            time.sleep(0.5)
except KeyboardInterrupt:
    print("\nStopped.")