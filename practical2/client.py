import xmlrpc.client
import os

HOST = '127.0.0.1'
PORT = 9000
FILENAME = 'test_rpc.txt'

def send_file():
    proxy = xmlrpc.client.ServerProxy(f"http://{HOST}:{PORT}/")
    print(f"Connected to RPC Server at {HOST}:{PORT}")
    if not os.path.exists(FILENAME):
        print(f"File {FILENAME} not found! Please create it first.")
        return
    with open(FILENAME, "rb") as handle:
        binary_data = handle.read()
        response = proxy.upload_file(FILENAME, xmlrpc.client.Binary(binary_data))     
    print("Server Response:", response)
if __name__ == '__main__':
    send_file()