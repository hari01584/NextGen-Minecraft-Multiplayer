import threading
import time
import config
import requests
import stun
from codecs_x import parse_message
from codecs_x import simple_data_dump

API_URL_PUSH = "http://vortex.skullzbones.com/api/lobby/attacher.php"
API_URL_HOST_SERVER = "http://vortex.skullzbones.com/api/lobby/host_server.php"

def attach_to_backround_server_listen(): 
    while True:
        time.sleep(3)
        heads = {'uid': config.ID,'token': config.password}
        x = requests.post(API_URL_PUSH, headers = heads)
        if(parse_message(x.text)[0] == 1):
            print("New Message"+str(parse_message(x.text)[1]))


def createserver():
    svn = input("[-] Server Name:")
    mcv = "1.16.2.5"
    svpass = input("[-] Server Pass(Leave Empty For None):")
    nat_type, external_ip, external_port = stun.get_ip_info()

    
    if(nat_type == "Symmetric NAT"):
        print("[@] Sorry You Cant Host Free Servers On Mobile Data/Cellular Connections, Upgrade To Silver Plan To Access This!!")

    print("[@] To Host Servers You Need To Port Forward Server Port (UDP:98554)")
    x = int(input("[@] Did You Successfully Forwarded Port For Minecraft?? [Enter y/n] {Enter n to get instructions about how to do it!}"))
    if(x.lower() == 'y'):
        print("Making Server And Checking Port!")


    heads = {'uid': config.ID,'token': config.password}
    payload = simple_data_dump({'server_name': svn,'mc_ver': mcv,'server_pass': svpass,'ext_ip': external_ip,'ext_port': external_port})
    x = requests.post(API_URL_HOST_SERVER, data=payload, headers = heads)
    print(parse_message(x.text)[1])
    if(parse_message(x.text)[0] == -1):
        return
    else:
        attach_to_backround_server_listen()
