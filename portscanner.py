import socket
import threading
import concurrent.futures

the_lock = threading.Lock()
ip = input('>>> ')

def portscanner(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	try:
		s.connect((ip, port))
		s.close()
		with the_lock:
			print(f'{port} Opened!')
	except:
		pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as x:
	for port in range(1024):
		x.submit(portscanner, ip, port + 1)