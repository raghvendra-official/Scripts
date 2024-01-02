# combine

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_request_broadcast = broadcast / arp_request  # creating new packet and then combining the above two packet
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()
    # show use to display more detail properties of object

scan("192.168.1.1/24")