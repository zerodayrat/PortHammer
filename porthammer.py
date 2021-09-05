#!/bin/python3

import sys
import socket
import argparse
import banner
from colorama import Fore

GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET = Fore.RESET

banner.print_banner()

if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-p1','--port1',required=True,type=int,help="Enter starting Port")
	parser.add_argument('-p2','--port2',required=True,type=int,help="Enter Ending Port")
	parser.add_argument('-t','--target',required=True,help="Enter Target IP")

	args = parser.parse_args()

	target = socket.gethostbyname(args.target)

print(f"\n\n{RED}+--------------------------------------+")
print(f"TARGET :",args.target)
print("Staring Port:",int(args.port1))
print("Ending Port: ",int(args.port2))
print(f"{RED}+--------------------------------------+")

print(f"\n[+] Scan Started..")

try :	
	for port in range(int(args.port1),int(args.port2)):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) 
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"\n{GREEN}Port {{}} is open".format(port))
			s.close()

except KeyboardInterrupt:
	print(f"\n{RED}[x] Program Exited{RESET}")
	sys.exit()
	
except socket.gaierror:
	print(f"\n{RED}[-] Error : Hostname couldn't be Resolved{RESET}")
	sys.exit()
except socket.error:
	print(f"\n{RED}[-] Socket Error")
	sys.exit()

print(f"\n{YELLOW}[+] Scan Finished :)")
