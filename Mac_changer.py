import subprocess  # Used to interact with terminal
import optparse  # Used to get attribute by the user(parsing)

# Using OOPS
parser = optparse.OptionParser()  # It is a Class (Object)

parser.add_option("-i", "--interface", dest="interface",
                  help="Interface to change its MAC address")  # learning the child or telling the child
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")  # learning the child or telling the child

(options, arguments) = parser.parse_args()  # return argument & value
# to access value do options.interface / options.new_mac

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# It can not hijacked
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

# Method-1
# interface = input("Enter the interface > ")
# new_mac = input("Enter the new MAC > ")
#
# print("[+] Changing MAC address for " + interface + " to " + new_mac)

# It can easily Hijack
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

# It can not hijack
# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw","ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])
