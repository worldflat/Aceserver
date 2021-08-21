import os
import json
import pathlib
json_path = os.path.abspath('profile.json')
port = None

with open(json_path) as f:
    jsn = json.load(f)
    port = jsn["server"]["setting"]["port"]
    type = jsn["option"]["type"]
    dir = jsn["server"]["setting"]["share_dir"]
    address = jsn["server"]["setting"]["address"]
    cgi_dir = jsn["server"]["setting"]["cgi_dir"]
    cgi_dir = str(pathlib.Path(os.path.abspath('core.py')).parents[0]) + cgi_dir
    public_dir = str(pathlib.Path(os.path.abspath('core.py')).parents[0]) + dir
    print(public_dir)

    if (type == "http"):
        from lib.Http import Httpserver
        s = Httpserver(address, port, public_dir)
        s.runserver()
    elif (type == 'socket'):
        from lib.Socket import Socketserver
        s = Socketserver(address, port)
        s.runserver(1200)
    elif (type == 'cgi'):
        from lib.Cgi import CGIServer
        s = CGIServer(port, address, cgi_dir)
        s.runserver()
