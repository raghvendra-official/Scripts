import subprocess  # Used to interact with terminal
import optparse  # Used to get attribute by the user(parsing)


# functions
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()  # returning the value of parser
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")  # code to handle error
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac, use --help for more info")  # code to handle error
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
