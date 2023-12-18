import socket

IP = '192.168.0.74'
PORT = 25000

main_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
main_sock.bind((IP, PORT))

while True:
    try:
        print("Waiting")
        data,_ = main_sock.recvfrom(2048)
        print(f"[MESSAGE] >> {' '.join([i[2:].zfill(2) for i in map(hex, list(data))])}")
    except KeyboardInterrupt:
        break
    except socket.error as E:
        if E.errno == 10054:
            print(f"[INFO][WinError 10054] Check client port number")
            continue
        elif E.errno == 10038:
            print(f"[INFO][WinError 10038] socket closed")
        else:
            print(f"[ERROR] socket recv failed")
        break
    