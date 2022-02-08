# ARP-Spoofer
This allows your machine to use the MAC address of a target router, giving other computers connected to the network an impression that your machine is the router. This allows communication to flow from your targets computer to your computer.

Libraries used : scapy

## How It Works
- Enter your target's IP address
- Enter your target router's IP address
    - In the event you have problems recieving target's IP address, stay tuned for my IP Ping Verify Program! 
- This will follow on to get the MAC/Physical address of the router by identifying the "dst" & "pdst" elements of the ARP
- Now we have the MAC address of the router!
- The next step is to spoof your machine to have the same MAC address as the router
    - This is to ensure that your target computer thinks that your machine is the router that its communicating to.
- Now we have tricked the target machine into thinking that you are the router and it feels free to communicate.
- Here's a catch :
    - The target machine has its own firewalls and security protocols.
    - Hence, it will refresh the details of devices within a time period. 
    - In order to beat this refresh system, there is a while loop in place to constantly send packets.
- If we execute the program without ipv4 forwarding, this acts as a DoS (Denial of Service) attack.
- This is caused by the fact that the target machine will not be able to access the Internet
