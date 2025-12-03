import xmlrpc.client
import os

HOST = '127.0.0.1'
PORT = 9000
FILENAME = 'test_rpc.txt' # Tạo file này trước khi chạy để test

def send_file():
    # Kết nối đến Server qua RPC Proxy
    proxy = xmlrpc.client.ServerProxy(f"http://{HOST}:{PORT}/")

    print(f"Connected to RPC Server at {HOST}:{PORT}")
    
    if not os.path.exists(FILENAME):
        print(f"File {FILENAME} not found! Please create it first.")
        return

    with open(FILENAME, "rb") as handle:
        # Đọc dữ liệu file
        binary_data = handle.read()
        
        # Gọi hàm từ xa: upload_file(tên_file, dữ_liệu_gói_binary)
        # Lưu ý: Phải dùng xmlrpc.client.Binary để gửi dữ liệu nhị phân an toàn
        response = proxy.upload_file(FILENAME, xmlrpc.client.Binary(binary_data))
        
    print("Server Response:", response)

if __name__ == '__main__':
    send_file()