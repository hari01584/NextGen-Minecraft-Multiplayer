import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 61873

BUFFER = 2048


LLCLIENT_IP = ''
LCLIENT_PORT = 0

SSERVER_PORT = 59285
SSERVER_IP = '139.59.82.105'


server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + ":" + str(server_port))

payload, client_address = sock.recvfrom(BUFFER)
LLCLIENT_IP = client_address[0]
LCLIENT_PORT = client_address[1]
print("LIP:"+LLCLIENT_IP+" LPORT:"+str(LCLIENT_PORT))

while True:
        payload, client_address = sock.recvfrom(BUFFER)
        if(client_address[1] == LCLIENT_PORT):
                client_address = (SSERVER_IP,SSERVER_PORT)
        else:
                client_address = (LLCLIENT_IP,LCLIENT_PORT)

        print("Send data to " + str(client_address))
        sent = sock.sendto(payload, client_address)
