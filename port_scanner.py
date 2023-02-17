import ipaddress
from scapy.layers.inet import *
from scapy.all import *
import re
import socket


def port_scanner():
    # host_name = socket.gethostname()
    # host_ip = socket.gethostbyname(host_name)
    # print(f"hostname : {host_name}")
    # print(f"host ip : {host_ip}")

    print("\n\n\n\n=== PORT SCANNER ===")
    port_regex = re.compile("([0-9]+){1,5}-([0-9]+){1,5}")
    ip_regex1 = re.compile("^\d")
    ip_regex2 = re.compile("^www\.")

    while 1:
        ip_address_input = input("Type Destination IP Address or Domain Address : ")
        try:
            ip_regex1_valid = ip_regex1.search(ip_address_input.replace(" ", ""))
            ip_regex2_valid = ip_regex2.search(ip_address_input.replace(" ", ""))
            if ip_regex1_valid:
                ip_address = ipaddress.ip_address(ip_address_input)
                break
            elif ip_regex2_valid:
                ip_address = ipaddress.ip_address(ip_address_input)
                break
        except:
            print("This is wrong type or format of IP address")

    while 1:
        port_start = 0
        port_end = 65335
        port_range = input("Type the port range ( ex: 0-65535 ) : ")
        port_range_valid = port_regex.search(port_range.replace(" ", ""))
        if port_range_valid:
            port_start = int(port_range_valid.group(1))
            port_end = int(port_range_valid.group(2))
            break

    valid_ports = []
    for port in range(port_start, port_end + 1):
        send_packet = IP(dst=ip_address.compressed) / \
                      TCP(dport=port, flags="S")
        response = sr1(send_packet, timeout=0.1, verbose=0)
        if response and response[TCP].flags == "SA":
            valid_ports.append(port)
        else:
            print("port", port, "[ X ]")

    print("\n\n=========[ VALID PORT ]=========")
    for port in valid_ports:
        print("port", port)
