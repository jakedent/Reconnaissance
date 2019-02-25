import socket
import threading

def scanner():

    target = input("Insert target URL / IP : ")

    def scan(ports):
        p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        p.settimeout(0.5)

        try:
            connect = p.connect((target, ports))
            print("Port : ", ports, " Open")
            connect.close()
        except:
            pass

    i = 1
    for z in range(1, 100):
        thread = threading.Thread(target=scan, kwargs={'ports': i})
        i += 1
        thread.start()


if __name__ == '__main__':
    scanner()
