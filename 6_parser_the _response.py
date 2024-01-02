import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # it tell the destination to packet of scapy.srp (MAC)
    arp_request_broadcast = broadcast / arp_request  # creating new packet and then combining the above two packet
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose = False) [0]                # we create an Ether that's why we use 'srp' instead of "sr" that send and recieve a response.it return two list one answered value and another unanswered value
                                                                                                    # verbose help to not display unwanted content
    
    print("IP\t\t\tMAC Address\n------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print("-------------------------------------------")

scan("192.168.1.1/24")