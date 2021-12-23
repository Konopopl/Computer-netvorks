import sqlalchemy
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
import json
import sys

def add(o, s, key):
    if isinstance(o, dict):
        for k in o:
            add(o[k], s.setdefault(key, {}), k)
    elif isinstance(o, list):
        for k in o:
            add(k, s, key)
    else:
        s[key][o] = s.setdefault(key, {}).setdefault(o, 0) + 1
        
                


keys = ("id","name","description","version","definition","deployed_at","created_at","updated_at","visibility","lifecycle_state","picture","api_lifecycle_state","environment_id","background","disable_membership_notifications")

engine = create_engine("postgresql://postgres:postgres@localhost:5432")
apis = engine.execute("select * from gravitee.apis")
o = {"key" : {}}
pairs = {}
sample = {}
size = 0
for raw in apis:
    size += 1
    for k,v in zip(keys,raw):
        if k == "definition":
            v = json.loads(v)
            add(v, o, "key")
            sample = v
            hosts = [x["path"] for x in v["proxy"]["virtual_hosts"]]
            if len(hosts) != 1:
                print("warning: hosts more than 1")
                print(hosts)
            endpoints = [y["target"] for x in v["proxy"]["groups"] for y in x["endpoints"]]
            for host in hosts:
                if host in pairs:
                    print("warning: host %s is dublicated" % host)
                pairs[host]=endpoints
with open("config.json", "w") as file:
    file.write(json.dumps(pairs, indent=4))
            
