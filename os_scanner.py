import subprocess


def enum_os():
    target = input("Target IP : ")
    print("\nEnumerating OS details from", target)
    subprocess.call(['nmap', '-p', '445', '--script', 'smb-os-discovery', target])


if __name__ == '__main__':
    enum_os()