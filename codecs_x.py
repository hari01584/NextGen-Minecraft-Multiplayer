import json

CONST_CREDENTIALS_FILE = "credentials.txt"


def simple_data_dump(payload):
    return json.dumps(payload)

def parse_message(json_pay):
    if("message" in json_pay):
        return (json.loads(json_pay)["code"],"[0] "+json.loads(json_pay)["message"])
    else:
        return (0,"[$] Internet Problem Or Server Crash, Response Was Not Adequate!!")

def save_creds(json_pay):
    tree = json.loads(json_pay)["data"]
    with open(CONST_CREDENTIALS_FILE,"w") as f:
        f.write(simple_data_dump(tree))


def nested_data_parse(json_pay):
    obs = []
    js = json.loads(json_pay)["data"]
    for item in js:
        obs.append(item)

    return obs
