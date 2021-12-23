import json
with open("config.json") as file:
    config = json.loads(file.read())
output = \
"static_resources:\n\
  listeners:\n"

clusters = "  clusters:\n"

with open("envoy-config-listener-template.yml") as file:
    listener_template = file.read()
with open("envoy-config-cluster-template.yml") as file:
    cluster_template = file.read()
with open("envoy-config-endpoint-template.yml") as file:
    endpoint_template = file.read()

def find_address_and_port(url):
    parts = url.split("://")
    if len(parts) != 2:
        print("[WARNING] bad url: %s" % url)
        if len(parts) == 1:
            protocol = "http"
            address = url
        else:
            protocol = parts[0]
            address = "://".join(parts[1:])
    else:
        protocol, address = url.split("://")
    host = address.split("/")[0]
    parts = host.split(":")
    if len(parts) < 2 or parts[1] == "":
        if protocol == "http":
            port = 80
        elif protocol == "https":
            port = 443
        else:
            print("[WARNING] undefined port for url %s. used 80 by default" % url)
            port = 80
    else:
        port = parts[1]
    index = address.find("/")
    if index != -1:
        url = parts[0] + address[index:]
    else:
        url = parts[0]
    return url, port

i = 1
for service in config:
    output += listener_template % (i, service, i)
    clusters += cluster_template % (i, i)
    for endpoint in config[service]:
        address, port = find_address_and_port(endpoint)
        clusters += endpoint_template % (address, port)
    i += 1

output += clusters

with open("envoy-config-generated.yml", "w") as file:
    file.write(output)
