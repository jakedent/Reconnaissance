import subprocess


def find_hosts():
    target = input("Enter IP : ")
    try:
        # NSE script for finding hosts on remote IP.
        subprocess.call(['nmap', '-p', '80', '--script', 'hostmap-bfk.nse', target])
    except Exception as e:
        print("\nUnable to find hosts... {0}".format(e))


if __name__ == '__main__':
    find_hosts()
