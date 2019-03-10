import subprocess


def restart_services():
    interface = input("\nInsert interface (wlan0, etc) : ") 
    try:
        subprocess.call(['service', 'network-manager', 'restart'])
        subprocess.call(['iwconfig'])
    except Exception as e:
        print("\nUnable to run commands... {0}".format(e))
    try:
        subprocess.call(['airmon-ng', 'start', interface, '7'])
        subprocess.call(['airmon-ng', 'stop', interface + 'mon'])
        subprocess.call(['ifconfig', interface, 'up'])
    except Exception as e:
        print("\nUnable to restart network services on ", interface, "{0}".format(e))
    return


if __name__ == '__main__':
    restart_services()
