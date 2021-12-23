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
sample = {}
size = 0
for raw in apis:
    size += 1
    for k,v in zip(keys,raw):
        if k == "definition":
            add(json.loads(v), o, "key")
            sample = json.loads(v)
print(json.dumps(o["key"], indent=4))
print("\n\n\n")
print(json.dumps(sample, indent=4))
print(size)