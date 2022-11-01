import datetime
import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

class Utils:
    def __init__(self):
        self.datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def logs(self, message):
        print(f"[{self.datetime}] {message}")