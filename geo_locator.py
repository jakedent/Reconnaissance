import subprocess


def g_locate():
    # NSE script for tracing IP geo-location.
    target = input("\nTarget URL / IP : ")
    print("\nTracing geo-location of : ", target)
    subprocess.call(['nmap', '--traceroute', '--script', 'traceroute-geolocation.nse', '-p', '80', target])


if __name__ == '__main__':
    g_locate()
