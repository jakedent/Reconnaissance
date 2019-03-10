import subprocess


def enum_apps():
    print(
        "\nWARNING: \nThis NSE script brute forces web server paths to discover applications and is more aggressive than others. \nThe web server you run against will store logs in the thousands of error 404 bad HTTP requests.")
    usr_warning = input("Are you sure you want to run this script? : ")
    if usr_warning == "no":
        print("Returning to menu...")
    elif usr_warning == "yes":
        target = input("Enter target URL : ")
        try:
            subprocess.call(['nmap', '--script', 'http-enum', target])
        except Exception as e:
            print("\nCould not brute force with nmap NSE... {0}".format(e))
    else:
        print("Sorry, please type yes or no.")


if __name__ == '__main__':
    enum_apps()
