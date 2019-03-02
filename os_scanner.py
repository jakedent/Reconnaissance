import subprocess


def enum_os():
    target = input("Target IP : ")
    print("\nEnumerating OS details from", target, " using nmap.")
    subprocess.call(['nmap', '-p', '445', '--script', 'smb-os-discovery', target])
    print("\nEnumerating OS details from", target, "using xprobe2")
    print("\nChecking if host is live...")
    try:
        subprocess.call(['xprobe2', target])
        print("\nHost is live!")
    except Exception as e:
        print("\nUnable to connect to host - {0}.".format(e))

    print("\nEnumerating OS details through TCP...")
    try:
        subprocess.call(['xprobe2', '-T', '1-2000', target])
    except Exception as e:
        print("\nUnable to gather OS details - {0}".format(e))



if __name__ == '__main__':
    enum_os()
