# ┌──────────────────────────────────┐
# │ This code was created by p-i-c-o │
# │ GitHub:   www.github.com/p-i-c-o │
# │                                  │
# │ No referral is required!         │
# │ This was created for the world.  │
# └──────────────────────────────────┘

# ------------------------- IMPORTS -------------------------

import socket

# ------------------------ FUNCTIONS ------------------------

def send_data(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    message = ""

    while message != "exit":
      message = input("[>]  ")
      s.sendall(message.encode())

    s.close()

def receive_data(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    print("Waiting for connection...")
    conn, addr = s.accept()
    print(f"Connected to {addr}")

    data = ""
    while data != "end":
      data = (conn.recv(1024)).decode()
      print("Received:", data)
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

# ------------------------ MAIN CODE ------------------------

if __name__ == "__main__":
    main()
