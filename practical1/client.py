import socket
import os

HOST = '127.0.0.1'
PORT = 65432
FILENAME = 'test_file.txt' 

def send_file():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    filesize = os.path.getsize(FILENAME)

    client_socket.send(f"{FILENAME}|{filesize}".encode())
    
    with open(FILENAME, "rb") as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            client_socket.send(chunk)
            
    print("Đã gửi file thành công!")
    client_socket.close()

if __name__ == "__main__":
    send_file()