arp_req=scapy.ARP()

scapy.ls(scapy.ARP())

import scapy.all as scapydef scan(ip):# scapy.arping(ip)arp_req=scapy.ARP(pdst=ip)broadcast = scapy.Ether()scapy.ls(scapy.Ether())scan("192.168.2.1/24")

arp_sum = broadcast/arp_req

import scapy.all as scapydef scan(ip):# scapy.arping(ip)arp_req=scapy.ARP(pdst=ip)broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")arp_sum = broadcast/arp_reqans, unans= scapy.srp(arp_sum, timeout=1, verbose=False)print("IP\t\t\t\tMAC")print("-------------------------------------------")for a in ans:print(a[1].psrc + "\t\t\t" + a[1].hwsrc)scan("192.168.2.1/24")

import scapy.all as scapydef scan(ip):# scapy.arping(ip)arp_req=scapy.ARP(pdst=ip)broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")arp_sum = broadcast/arp_reqans, unans= scapy.srp(arp_sum, timeout=1, verbose=False)print("IP\t\t\t\tMAC")print("-------------------------------------------")for a in ans:print(a[1].psrc + "\t\t\t" + a[1].hwsrc)scan("192.168.2.1/24")