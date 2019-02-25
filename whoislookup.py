# Who Is Lookup
import whois
import socket
import subprocess




def look_up():
    target = input("\nDomain name : ")
    try:
        data = whois.query(target)
        print("\nWebsite name : ", data.name)
        print("\nWebsite IP : ", socket.gethostbyname(target))
        print("\nRegistrar : ", data.registrar)
        print("\nCreation date : ", data.creation_date)
        print("\nExpiration date : ", data.expiration_date)
        print("\nLast updated : ", data.last_updated)
        print("\nName servers : ", data.name_servers)
        # NSE script for dns enumeration.
        print("\nEnumerating sub domains for : ", target)
        subprocess.call(['nmap', '-p', '80', '--script', 'dns-brute.nse', target])
    except Exception as e:
        print("Domain not recognised.".format(e))


if __name__ == '__main__':
    look_up()
