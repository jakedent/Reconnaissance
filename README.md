# GhostRecon - a Kali Linux toolkit.
# Automated Reconnaissance.

GhostRecon provides an automation tool for each step of the recon phase: 

   1. Gather initial information
   2. Determine the network range
   3. Identify active machines
   4. Discover open ports and access points
   5. Fingerprint the operating system
   6. Uncover services on ports
   7. Map the network

# Installation : 

Update Kali : sudo apt-get update && sudo apt-get upgrade

Python libraries : pip3 install whois

Download GhostRecon repo.

# Usage : 
Built for Kali Linux - utilises tools such as Arp-Scan, NMap and xprobe. 

Open terminal. 

Change to the GhostRecon directory and type : sudo python3 main.py

# Menu breakdown : 
   1. Advanced WHOIS lookup - lists general WHOIS lookup information + sub domains. 
   2. List network devices - list the devices connected to your network.
   3. WHOAMI - hilarious take on WHOIS and lists your configurations and details.
   4. URL / IP port scanner - enter a URL or IP and scan for open ports.
   5. Promiscuous AP scan - enter monitor mode and scan for access points.
   6. Spoof / reset MAC address - generates and spoofs your mac address. 'Reset [port]' resets mac configurations. 
   7. Scan host on remote IP - list the devices connected to  remote IP.
   8. Scan IP for OS details - enumerate operating system details from IP.
   9. URL / IP geo-locater - discover geographical location of an IP address.
   10. Web server application scan - list services and apps running on a web server, very loud.
   11. Reset network services - for use after promiscuous mode.

![gr](https://user-images.githubusercontent.com/10816773/53376627-e399f800-3956-11e9-8aa4-a3cb28d0ad82.png)

Happy reconnaissance! 
