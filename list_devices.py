import subprocess


def map_network():
    subprocess.call(['arp-scan', '-l'])


if __name__ == '__main__':
    map_network()
