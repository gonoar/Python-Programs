from socket import *

def port_scan(ip,start,end):
	open_ports=[]
        scan_ip = gethostbyname(ip)
        for i in range(start,end+1):
		print('Scanning Port ',i)
                sock = socket(AF_INET,SOCK_STREAM)
		sock.settimeout(20)
		result=sock.connect_ex((scan_ip,i))
		if result == 0:
			open_ports.append(i)
	print("Following port(s) are open:")
	for i in open_ports:
		print(i)
	if(len(open_ports)==0):
		print("None!!")

ip=raw_input("Enter ip or host name:")
start,end=raw_input("Enter port range to scan(Eg. 50-100,50):").split('-')
port_scan(ip,int(start),int(end))

