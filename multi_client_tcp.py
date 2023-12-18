from threading import Thread, Event
import time
import socket

def send_mesg(mesg: bytes, _event: Event, addr: tuple[str, int]) -> None:
    sock = socket.socket()
    sock.connect(addr)
    while True:
        if _event.is_set():
            ret = sock.send(mesg)
            res = sock.recv(1024)
            print(f"{addr} finished send mesg {ret, res}")
            time.sleep(0.5)
            break
    sock.close()
    # print(f"{addr} finished send mesg")

if __name__ == "__main__":
    mesg = bytes(map(lambda x: int(x, 16), '00 01 00 00 00 06 01 05 00 00 ff 00'.split()))
    send_event = Event()
    send_event.clear()
    thread_list = [Thread(target=send_mesg, args=(mesg, send_event, i)) for i in [('127.0.0.1', 502), ('127.0.0.1', 503), ('127.0.0.1', 504), ('127.0.0.1', 505)]]
    for i in thread_list:
        i.start()
    time.sleep(0.5)
    send_event.set()

# if __name__ == "__main__":
#     mesg = bytes(map(lambda x: int(x, 16), '00 01 00 00 00 06 01 05 00 02 00 00'.split()))
#     send_event = Event()
#     send_event.clear()
#     T = Thread(target=send_mesg, args=(mesg, send_event, ('10.129.41.60', 502)))
#     T.start()
#     time.sleep(0.5)
#     send_event.set()