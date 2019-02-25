# Check host details
import socket
import subprocess


def c_host():
    host = socket.gethostname()
    ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip.connect(("8.8.8.8", 80))
    print("\nYour Computer Name: " + host)
    print("\nYour IP Address: " + ip.getsockname()[0])
    ip.close()
    try:
        print("\nYour Wireless MAC Address : " + subprocess.check_output("ifconfig wlan0 | grep ether", shell=True).decode()[
                                             14:])
    except Exception as e:
        print("\n No connection active.".format(e))
    try:
        print("Your Wired MAC Address : " + subprocess.check_output("ifconfig eth0 | grep ether", shell=True).decode()[
                                             14:])
    except Exception as e:
        print("\n No connection active.".format(e))

if __name__ == '__main__':
    c_host()
