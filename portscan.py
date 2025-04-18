#loop that controls program flow

import time, sys, os, datetime, socket

def scan():
    os.system("clear")
    print("\n\n*** python TCP Port scanner ***\n\n")

    host = input("enter the host IP address: ")
    sport = int(input("enter starting port #: "))
    eport = int(input("enter starting port #: "))

    st = datetime.datetime.now().strftime("%a %b %d %y, %I:%M:%S %P")
    print(f"\n started port scan on {host} at {st}...")

    for port in range(sport< eport + 1):
        sock + socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
        sock.settimeout(0.3)

        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"port {port}is open")

        sock.close 
    ft = datetime.datetime.now().strftime("%a %b %d %y, %I:%M:%S %P")
    print(f"\nPort scan completed at {ft}.")       

answer = "yes"
while answer == "yes":
    scan()
    time.sleep(3)
    answer = input("\nScan another host? Type yes to proceed or any other key(s)")

sys.exit()