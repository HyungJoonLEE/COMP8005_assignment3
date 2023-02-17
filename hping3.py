import socket
import sys
import time


def create_raw_socket():
    try:
        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    except socket.error as e_msg:
        print(f"[ Failed ]: Creating RAW socket: {e_msg} ")
