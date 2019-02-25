import subprocess

def restart_services():
    subprocess.call(['service', 'network-manager', 'restart'])
    subprocess.call(['iwconfig'])
    subprocess.call(['airmon-ng', 'start', 'wlan0', '7'])
    subprocess.call(['airmon-ng', 'stop', 'wlan0mon'])
    subprocess.call(['ifconfig', 'wlan0', 'up'])
    return


if __name__ == '__main__':
    restart_services()