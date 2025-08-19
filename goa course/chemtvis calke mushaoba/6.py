import time
import sys

def loading_screen(choice_option):
 for i in range(3):  # how many times it repeats
    for dots in range(4):  # "", ".", "..", "..."
        sys.stdout.write("\rLoading" + "." * dots + "   ")  # overwrite line
        
        time.sleep(0.5)  # delayc
        if i == 2 and dots == 3:
         

         if choice_option == "1":
           print("\rloading complete")


       # elif choice_option == "2"

           
        



loading_screen("1")
     
           

     

