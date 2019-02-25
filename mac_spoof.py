# spoof MAC address LINUX
import subprocess


def mac_func():
    print("\nWARNING: Run option 3 in the menu and note your current MAC configurations.")
    print("\nType 'reset wlan0' or 'reset eth0' for reset mode.")
    mac_select = input("\nSelect which port to change (wlan0 or eth0) (q = exit): ")
    if mac_select == "q" or mac_select == "quit":
        print("\nQuitting...")
        return
    elif mac_select == "wlan0":
        subprocess.call("ifconfig wlan0 down", shell=True)
        subprocess.call("ifconfig wlan0 hw ether 44:d1:01:52:74:48", shell=True)
        subprocess.call("ifconfig wlan0 up", shell=True)
    elif mac_select == "eth0":
        subprocess.call("ifconfig eth0 down", shell=True)
        subprocess.call("ifconfig eth0 hw ether 44:d1:01:52:74:48", shell=True)
        subprocess.call("ifconfig eth0 up", shell=True)
    elif mac_select == "reset wlan0":
        old_wlan = input("Insert old wireless mac address : ")
        subprocess.call("ifconfig wlan0 down", shell=True)
        subprocess.call("ifconfig wlan0 hw ether" + old_wlan, shell=True)
        subprocess.call("ifconfig wlan0 up", shell=True)
    elif mac_select == "reset eth0":
        old_eth = input("Insert old wired mac address : ")
        subprocess.call("ifconfig eth0 down", shell=True)
        subprocess.call("ifconfig eth0 hw ether " + old_eth, shell=True)
        subprocess.call("ifconfig eth0 up", shell=True)
    else:
        print("Invalid input. Type either wlan0 or eth0 to change MAC address.")


if __name__ == '__main__':
    mac_func()
