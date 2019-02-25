import subprocess


def find_hosts():
    target = input("Enter IP : ")
    # NSE script for finding hosts on remote IP.
    subprocess.call(['nmap', '-p', '80', '--script', 'hostmap-bfk.nse', target])


if __name__ == '__main__':
    find_hosts()