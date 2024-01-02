import scapy.all as scapy


def scan(ip):
    scapy.arping(ip)


scan("192.168.1.1")  # enter the value or range of an IP to be searched
