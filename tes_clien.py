import socket
from binascii import unhexlify
import time

hexr = "1c0000000000000001000000000000000100ffff00fefefefefdfdfdfd12345678005b4d4350453b58424f5820444f4e5420574f524b204845523b3430373b312e31362e31303b313b383b31313034313937303639373133303631383435303b6b736b736b733b43726561746976653b313b35313739373b35313739383b"
data = unhexlify(hexr)

target_address = ("192.168.42.129",38337)
bufferSize = 1024
#10.2.5.1
# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(1.0)
UDPClientSocket.bind(("0.0.0.0",50225))

while True:
    time.sleep(1)
    UDPClientSocket.sendto(data, target_address)
    try:
        msgFromServer = UDPClientSocket.recv(bufferSize).hex()
        msg = "Message from Server {}".format(msgFromServer)
        print(msg)
    except socket.timeout:
        continue
