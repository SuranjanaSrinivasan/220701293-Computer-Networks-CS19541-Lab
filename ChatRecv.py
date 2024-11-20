import socket
def start_server(host = '127.0.0.1', port = 12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        for i in range(5):
            data, addr = s.recvfrom(1024)
            print(f"Recieved from {addr}:{data.decode()}")
            chat = input().encode('utf-8')
            s.sendto(chat, addr)
start_server()
