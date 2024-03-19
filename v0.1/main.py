import socket

def send_data(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    message = input("Enter message to send: ")
    s.sendall(message.encode())
    s.close()

def receive_data(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    print("Waiting for connection...")
    conn, addr = s.accept()
    print(f"Connected to {addr}")
    data = conn.recv(1024)
    print("Received:", data.decode())
    conn.close()

def main():
    mode = input("Choose mode (1 for send, 2 for receive): ")
    if mode == '1':
        ip = input("Enter IP to send data to: ")
        port = int(input("Enter port: "))
        send_data(ip, port)
    elif mode == '2':
        port = int(input("Enter port to listen on: "))
        receive_data(port)
    else:
        print("Invalid mode!")

if __name__ == "__main__":
    main()
