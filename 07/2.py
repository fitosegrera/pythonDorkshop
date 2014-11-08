## Import Scapy module
from scapy.all import *
## Create a Packet Count var
packetCount = 0
## Define our Custom Action function
def customAction(packet):
    global packetCount
    packetCount += 1
    return "Packet #%s: %s ==> %s" % (packetCount, packet[0][1].src, packet[0][1].dst)
## Setup sniff, filtering for IP traffic
sniff(filter="ip",prn=customAction)