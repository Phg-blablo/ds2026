import os
from xmlrpc.server import SimpleXMLRPCServer

HOST = '127.0.0.1'
PORT = 9000

def save_uploaded_file(filename, file_data):
    """
    Hàm này sẽ được Client gọi từ xa (Remote Procedure).
    file_data: Dữ liệu binary của file được gói trong xmlrpc.client.Binary
    """
    print(f"Receiving file: {filename}")
    
    # file_data.data là bước giải nén dữ liệu từ gói RPC
    with open("uploaded_" + filename, "wb") as handle:
        handle.write(file_data.data)
        
    return f"Success: {filename} has been saved on server."

if __name__ == '__main__':
    server = SimpleXMLRPCServer((HOST, PORT))
    print(f"RPC Server listening on port {PORT}...")
    
    # Đăng ký hàm để Client có thể gọi
    server.register_function(save_uploaded_file, "upload_file")
    
    server.serve_forever()