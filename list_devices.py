import subprocess


def map_network():
    try:
        subprocess.call(['arp-scan', '-l'])
    except Exception as e:
        print("\nUnable to run arp-scan. {0}".format(e))


if __name__ == '__main__':
    map_network()
