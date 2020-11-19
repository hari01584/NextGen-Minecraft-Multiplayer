import config
from codecs_x import parse_message
from codecs_x import simple_data_dump
from codecs_x import nested_data_parse
from peerless import mc_bdcast
import requests

API_URL_HOST_LOBBY = "http://vortex.skullzbones.com/api/lobby/getservers.php"

def getlobby():
    heads = {'uid': config.ID,'token': config.password}
    x = requests.post(API_URL_HOST_LOBBY, headers = heads)
    if(parse_message(x.text)[0] == -1):
        return
    print("{:<10} {:<30} {:<30}".format('S.No','S.Name','Players'))
    servers = nested_data_parse(x.text)
    for i in range(len(servers)):
        it = servers[i]
        print("{:<10} {:<30} {:<30}".format(i+1,it['server_name'],int(it['players'])))
    x = int(input("[$] Enter Server Number To Start! (Or 0 To Refresh): "))
    if(x==0):
        getlobby()
    elif(x in range(1,len(servers)+1)):
        print("[$] Connecting. Server",x)
        mc_bdcast(servers[i-1])
        
    else:
        print("[$] Server Number Aint In List!!")

