import os
import requests
from crypt import salt
from codecs_x import simple_data_dump
from codecs_x import parse_message
from codecs_x import save_creds
from config import assign
import config

CONST_CREDENTIALS_FILE = "credentials.txt"
API_URL_REGISTER = 'http://vortex.skullzbones.com/api/user/management/register.php'
API_URL_LOGIN = 'http://vortex.skullzbones.com/api/user/management/quick_login.php'
API_URL_VALIDATE = 'http://vortex.skullzbones.com/api/user/management/validate.php'


def logon():
    if(not os.path.exists(CONST_CREDENTIALS_FILE)):
        print("[-] Looks Like You Aint Signin Here! Use 1 To Create New Account Or 2 To Signin!")
        while True:
            x = int(input("[-] Enter Command:"))
            if(x==1):
                #username = input("[-] Enter Your Username:")
                #email = input("[-] Enter Your Email:")
                #passw = input("[-] Enter Your Password:")


                username="Agornageee"
                email="hari01584@gmail.com"
                passw="notyeardad"
                payload = simple_data_dump({'username': username,'email': email,'password': salt(email,passw)})
                x = requests.post(API_URL_REGISTER, data = payload)
                print(parse_message(x.text)[1])
                if(parse_message(x.text)[0] == 1):
                    print("[-] Login Using Second Command Now Below :)")
                
            elif(x==2):
                #email = input("[-] Enter Your Email:")
                #passw = input("[-] Enter Your Password:")
                
                email="hari01584@gmail.com"
                passw="notyeardad"
                
                payload = simple_data_dump({'email': email,'password': salt(email,passw)})
                x = requests.post(API_URL_LOGIN, data = payload)
                if(parse_message(x.text)[0] == -1):
                    print(parse_message(x.text)[1])
                else:
                    print("[-] Success Login! Subsequent Logins Be Automatically Done, Please Dont Share "+CONST_CREDENTIALS_FILE+" As It Contains Your Sensitive Information!")
                    save_creds(x.text)
                    break

                
    assign()
    heads = {'uid': config.ID,'token': config.password}
    x = requests.post(API_URL_VALIDATE, headers = heads)
    if(parse_message(x.text)[0] == -1):
        print(parse_message(x.text)[1])
        print("[$] Login Again!!")
        os.remove(CONST_CREDENTIALS_FILE)
        logon()
