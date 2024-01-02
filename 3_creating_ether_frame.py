# using scapy create an  Ether frame
# it give the output that from our MAC the given MAC address is sent to all client

import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # it's a virtual that does not exist and receive all client
    print(broadcast.summary())
    # scapy.ls(scapy.Ether())    this is use to check all the field that we may use


scan("192.168.1.1/24")
