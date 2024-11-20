import socket
import time
def ping_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.settimeout(10)
            start = time.time()
            for i in range(5):
                print(i,"conversation (limit 4):")
                chat = input().encode('utf-8')
                s.sendto(chat,(host,port))
                data, addr = s.recvfrom(1024)
                print(f"Recieved {data.decode()} from {addr}")
            end = time.time()
            print(f"{end-start:.2f}")
        except socket.timeout:
            print("Request Time Out")
ping_server()
