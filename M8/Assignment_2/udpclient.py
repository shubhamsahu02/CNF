import socket
def main():
	host = '10.1.135.120'
	port = 5173
	server = ('10.1.135.120', 5095)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	message = input('--')
	while message != 'x':
		s.sendto(message.encode(), server)
		data, addr = s.recvfrom(1024)
		print('from server: ' + data.decode())
		message = input('--')
	s.close()
if __name__ == '__main__':
	main()
