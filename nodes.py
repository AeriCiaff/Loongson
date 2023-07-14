import socket
import json

with open("settings.json", "r", encoding="utf-8") as f:
    settings = json.load(f)

node_ip_dict = settings["node_ip_dict"]

timeout = 5

def get_parameters_dict(node:str):
    assert node in node_ip_dict,f"请求的节点{node}不在节点字典中"
    ip = node_ip_dict[node]
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        s.sendto(b'?', (ip, 8035))
        data, _ = s.recvfrom(1024)
        parameters_dict = json.loads(data.decode())
        return parameters_dict
    except (socket.timeout,ConnectionError):
        return dict(status=False)
    finally:
        s.close()