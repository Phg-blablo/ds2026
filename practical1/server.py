import socket
import os

HOST = '127.0.0.1'
PORT = 65432

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server đang lắng nghe tại {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Đã kết nối với {addr}")
        
        # B1: Nhận thông tin file (tên và kích thước)
        file_info = conn.recv(1024).decode()
        filename, filesize = file_info.split('|')
        filesize = int(filesize)
        
        print(f"Đang nhận file: {filename} ({filesize} bytes)")
        
        # B2: Mở file để ghi
        with open("received_" + filename, "wb") as f:
            bytes_received = 0
            while bytes_received < filesize:
                # Nhận từng chunk (1024 bytes)
                chunk = conn.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
                bytes_received += len(chunk)
                
        print("Đã nhận file thành công!")

if __name__ == "__main__":
    start_server()