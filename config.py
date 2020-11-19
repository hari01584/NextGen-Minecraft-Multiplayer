import json

ID=0
user_login=""
password=""
username=""
email=""
register=""
user_status=""
display_name=""

CONST_CREDENTIALS_FILE = "credentials.txt"


def assign():
    global ID,user_login,password,username,email,register,user_status,display_name
    with open(CONST_CREDENTIALS_FILE,"r") as f:
        tree = json.loads(f.read())
        ID=tree["ID"]
        user_login=tree["user_login"]
        password=tree["password"]
        username=tree["username"]
        email=tree["email"]
        user_status=tree["user_status"]
        display_name=tree["display_name"]
