import os
import sys
import time 

def vuln():
	print("  ====")
	ip  = input("  Enter ip: ")
	print("")
	print("... pinging " +ip)
	time.sleep(2)

	response = os.system("ping -c 1 -w2 " + ip + " > /dev/null 2>&1")
	if response == 0:
		print("..... \033[38;5;208m Connected \033[0;0m")
		print("")
		os.system("nmap -vv -sV  --top-ports --script vuln " +ip)
	else:
		print("is down!")
	


vuln()
