import socket
import os

HOST = '127.0.0.1'
PORT = 65432
FILENAME = 'test_file.txt' # Tạo file này trước khi chạy

def send_file():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Lấy kích thước file
    filesize = os.path.getsize(FILENAME)
    
    # B1: Gửi thông tin file (Giao thức: filename|filesize)
    client_socket.send(f"{FILENAME}|{filesize}".encode())
    
    # B2: Gửi nội dung file
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