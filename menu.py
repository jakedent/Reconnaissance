import sys
import time
import subprocess
import os
from list_devices import map_network
from checkhost import c_host
from whoislookup import look_up
from remote_host import find_hosts
from geo_locator import g_locate
from web_apps import enum_apps
from mac_spoof import mac_func
from os_scanner import enum_os
from port_scan import scanner
from restart_net import restart_services
# Main definition - constants
menu_actions = {}


# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    print("\033[1;32;40m \n")
    print('''
        ('-. .-.               .-')    .-') _   _  .-')     ('-.                               .-') _  
            ( OO )  /              ( OO ). (  OO) ) ( \( -O )  _(  OO)                             ( OO ) ) 
  ,----.    ,--. ,--. .-'),-----. (_)---\_)/     '._ ,------. (,------.   .-----.  .-'),-----. ,--./ ,--,'  
 '  .-./-') |  | |  |( OO'  .-.  '/    _ | |'--...__)|   /`. ' |  .---'  '  .--./ ( OO'  .-.  '|   \ |  |\  
 |  |_( O- )|   .|  |/   |  | |  |\  :` `. '--.  .--'|  /  | | |  |      |  |('-. /   |  | |  ||    \|  | ) 
 |  | .--, \|       |\_) |  |\|  | '..`''.)   |  |   |  |_.' |(|  '--.  /_) |OO  )\_) |  |\|  ||  .     |/  
(|  | '. (_/|  .-.  |  \ |  | |  |.-._)   \   |  |   |  .  '.' |  .--'  ||  |`-'|   \ |  | |  ||  |\    |   
 |  '--'  | |  | |  |   `'  '-'  '\       /   |  |   |  |\  \  |  `---.(_'  '--'\    `'  '-'  '|  | \   |   
  `------'  `--' `--'     `-----'  `-----'    `--'   `--' '--' `------'   `-----'      `-----' `--'  `--'
    ''')
    print("\nCreated by : Jacob Dent")
    print("\nMain Menu\n")
    print("1. Advanced WHOIS lookup.")
    print("2. List network devices.")
    print("3. WHOAMI (host info).")
    print("4. URL / IP port scanner.")
    print("5. Promiscuous AP scan.")
    print("6. Spoof / reset MAC address.")
    print("7. Scan hosts on remote IP.")
    print("8. Scan IP for OS details.")
    print("9. URL / IP geo-locator.")
    print("10. Web server application scan.")
    print("11. Reset Network Services.")
    print("a. About GhostRecon.")
    print("h. How to use.")
    print("q. Exit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return


# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid menu choice, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1
def menu1():
    print("\n1. Advanced WHOIS lookup.\n")
    look_up()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print("\n2. List network devices.\n")
    print("\nMapping network...")
    time.sleep(0.5)
    map_network()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return


# Menu 3
def menu3():
    print("\n3. WHOAMI details.\n")
    c_host()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return


# Menu 4
def menu4():
    print("\n4. Port scanner.\n")
    scanner()
    print("Scanning...")
    time.sleep(10)
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return


# Menu 5
def menu5():
    print("\n5. Promiscuous AP Scanner.")
    time.sleep(1)
    print("\nWARNING: run option 7 from the menu and reset network services after scanning.")
    time.sleep(3)
    print("\nRun as long as needed. Use ctrl+c to exit scan window.")
    time.sleep(1)
    print("\nEnabling promiscuous mode on network card...")
    time.sleep(1)
    print("\nScanning...")
    time.sleep(1)
    subprocess.Popen(['gnome-terminal', '-e', 'python ./ap_scanner.py'], stdout=subprocess.PIPE)

    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return


# Menu 6
def menu6():
    print("\n6. MAC Spoofer\n")
    mac_func()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return

# Menu 7
def menu7():
    print("\n7. Remote IP host scanner.")
    find_hosts()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return

# Menu 8
def menu8():
    print("\n8. OS details IP scanner.")
    enum_os()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return

# Menu 9
def menu9():
    print("\n9. Geo-locator.")
    g_locate()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return

# Menu 10
def menu10():
    print("\n10. Brute force DNS.")
    enum_apps()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return

# Menu 11
def menu11():
    print("\n11. Reset Network Services.")
    time.sleep(1)
    restart_services()
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return

# Menu 12
def menu12():
    print("\n\na. About GhostRecon")
    print(
        "\nWith no infringement on the Tom Clancy franchise intended. \n\nGhostRecon is a 'stealthy' yet simple reconnaissance tool.\n")
    print("\nCreated by Jacob Dent. \n\nRepository : https://github.com/jakedent/GhostRecon \n")
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return


# Menu 13
def menu13():
    print("\nh. How to use GhostRecon.")
    print("\nBuilt for Kali.\n\nRun as sudo.")
    print("\nMenu options 1-11 will launch each tool respectively.\n")
    print("\nPromiscuous AP scan: \nAfter scan is complete, reset network services using option 11. \nSome tools may not work without active network adapters.")
    print("\nResetting MAC instructions: \nNote previous mac configurations. \nLaunch MAC Spoofer tool, type: reset wlan0 or reset eth0. \nPaste old MAC address as required.")
    print("\nGhostRecon")
    print("b. Back")
    print("q. Quit")
    choice = input("\nType here :  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit_app():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '6': menu6,
    '7': menu7,
    '8': menu8,
    '9': menu9,
    '10': menu10,
    '11': menu11,
    'a': menu12,
    'h': menu13,
    'b': back,
    'q': exit_app,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
