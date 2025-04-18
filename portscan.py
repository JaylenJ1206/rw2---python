#loop that controls program flow

import time, sys

def scan():
    print("i'm inside of scan")




answer = "yes"
while answer == "yes":
    print (" this is the 1st thing that prints")
    scan()
    time.sleep(3)
    answer = input("\nScan another host? Type yes to proceed or any pther key(s)")

sys.exit()