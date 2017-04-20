#/usr/bin/python
#Author_name = Rajkumar Pandi
#Date = 04/19/2017

import socket
import random, time, sys
from scapy. all import *

def main():
    dip = "192.168.1.3"
    sip = "192.168.1.1"
    dp = int(sys.argv[1])

    """Send SYN packet"""
    start = time.time()
    ip_packet = IP(src=sip,dst=dip)
    syn_packet = TCP(sport = 5556,dport=dp,flags='S',seq=1000)
    packet = ip_packet/syn_packet
    synack_response = sr1(packet)

    """send ACK packet"""
    if synack_response:
        temp = synack_response.seq
        myack = temp+1
        ack_packet = TCP(sport=5556,dport=dp,flags='A',seq=synack_response.ack,ack=myack)
        send(ip_packet/ack_packet)

        """Send payload packet"""
        payload = "FLOCC"
        payload_packet = TCP(sport=5556,dport=dp,flags ='PA',seq=synack_response.ack,ack=myack)
        p = ip_packet/payload_packet/payload
        server_resp = sr1(p,timeout=1)
        seq1 = server_resp.ack

        payload_packet2 = TCP(sport=5556,dport=dp,flags='PA',seq=seq1,ack=server_resp.seq)
        payload2 = "INAUCINIHILIP"
        p1 = ip_packet/payload_packet2/payload2
        server_resp1 = sr1(p1,timeout=1)
        seq2 = random.randint(1,26)

        payload_packet3 = TCP(sport=5556,dport=dp,flags='PA',seq=seq1,ack=server_resp1.seq)
        payload3 = "ILIFICATION"
        p2 = ip_packet/payload_packet3/payload3
        send(p2)

    else:
        print "I am root buhaha !"
        stop = time.time()
        duration = stop-start
        print(duration)

if __name__ == "__main__":
    main()

