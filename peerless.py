import socket
import sys
from binascii import unhexlify
import socket
import time


def sver(target_ip):
    pass


def mc_bdcast(serverData):
    print(serverData)
    CLIENT_IP = ''
    CLIENT_BROD_PORT = 0

    
    BrodcastSock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    BrodcastSock.settimeout(1.0)
    BrodcastSock.bind(("",19132))
    bufferSize = 64
    print("Open Your Game And Go To LAN Tab!!")
    while True:
        time.sleep(1)
        #BrodcastSock.sendto(data, target_address)
        try:
            payload, client_address = BrodcastSock.recvfrom(bufferSize)
            if(int(payload[0]) == 1):
                CLIENT_IP = client_address[0]
                CLIENT_BROD_PORT = client_address[1]
                print(CLIENT_IP," Asking For Connection On ",str(CLIENT_BROD_PORT)+" Accepting Connection!")
                break
            msg = "Message from Server {}".format(msgFromServer)
            print(msg)
        except socket.timeout:
            continue
    BrodcastSock.close()

    #Host_Name = serverData['server_name']
    #MC_V = serverData['server_mcv']
    #Host_Id = serverData['host_id']
    #ConnEctedP = serverData['players']

    Host_Id = 5
    MC_V = "1.16.4"
    ConnEctedP = 3
    Host_Name = "BABBBBB"    

    hexr = "1c0000000000000001000000000000000100ffff00fefefefefdfdfdfd12345678"
    MOTD_S = "MCPE;{};407;{};{};8;11041970697130618450;{};Creative;1;51797;51798;".format("Host "+str(Host_Id)+" Server!",MC_V,ConnEctedP,Host_Name)
    hexr += '{:04x}'.format(len(MOTD_S))
    hexr += (MOTD_S.encode('utf-8')).hex()
    data = unhexlify(hexr)

    target_address = (CLIENT_IP,CLIENT_BROD_PORT)
    bufferSize = 1024
    #10.2.5.1
    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.settimeout(1.0)
    UDPClientSocket.bind(("",51797))

    while True:
        time.sleep(1)
        UDPClientSocket.sendto(data, target_address)
        try:
            msgFromServer = UDPClientSocket.recv(bufferSize).hex()
            msg = "Message from Server {}".format(msgFromServer)
            print(msg)
        except Exception:
            continue
