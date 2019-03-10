import subprocess


def promise_ap():
    interface = input("\nInterface name (wlan0, etc) : ")
    try:
        subprocess.call(['airmon-ng', 'start', interface])
        subprocess.call(['airodump-ng', 'stop', interface])
        subprocess.call(['airmon-ng', 'check', 'kill'])
    except Exception as e:
        print("\nCould not initiate Airmon-ng. {0}".format(e))
    try:
        subprocess.call(['airodump-ng', interface + 'mon'])
    except Exception as e:
        print("\nUnable to start promiscuous mode on ", interface, "{0}".format(e))
    return


if __name__ == '__main__':
    promise_ap()
