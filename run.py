import os
import requests
from codecs_x import simple_data_dump
from codecs_x import parse_message
from user_management import logon
from listen_push import createserver
from lobby import getlobby
import config

print("[-] Welcome To Minecraft Multiplayer Python Bootstraper!!")
print("[-] Program Made By Agent_Orange#9852 (Discord)")
print("[-] Current Version a1.0")


logon()
print("[$] Logon Success! Going To Next Part!")


while True:
    print("[-] What Would You Like To Do?\n[-] 1.Host Server\n[-] 2.Join Server")
    x=int(input("[$] Enter Command:"))
    if(x==1):
        createserver()
    if(x==2):
        getlobby()
