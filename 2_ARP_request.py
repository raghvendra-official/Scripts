# using scapy create an  ARP request

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # given an ip to directed
    print(arp_request.summary())
    # scapy.ls(scapy.ARP())  this is use to check all the field that we may use


scan("192.168.1.1/24")