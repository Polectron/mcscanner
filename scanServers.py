#-*-coding:utf8;-*-
import sys
import mcstatus
import json

usable = 0
total = 0
discarded = 0

f = open("MCservers.json")
servers = json.loads(f.read())
f.close()

j = open("servers.json")
open_servers = json.loads(j.read())
j.close()

total = len(servers)

for server in servers:
    mcserver = mcstatus.MinecraftServer(server["ip"],int(server["ports"][0]["port"]))
    
    try:
        status = mcserver.status()
        print(server["ip"])
        open_servers.append(server["ip"])
        usable += 1
        print("The server has {0} players, version: {1}".format(status.players.online,status.version.name, status.description))
    except:
        discarded+=1

    print("\rFound: {0} servers, {1} discarded, {2} total".format(usable,discarded,total ))
print("{0} open servers found".format(usable))
j = open("servers.json","w")
j.write(json.dumps(open_servers))
j.close()
