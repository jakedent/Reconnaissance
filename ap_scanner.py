import subprocess


def promise_ap():
    subprocess.call(['airmon-ng', 'start', 'wlan0'])
    subprocess.call(['airodump-ng', 'stop', 'wlan0'])
    subprocess.call(['airmon-ng', 'check', 'kill'])
    subprocess.call(['airodump-ng', 'wlan0mon'])
    return


if __name__ == '__main__':
    promise_ap()