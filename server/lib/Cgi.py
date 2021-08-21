from http.server import HTTPServer, CGIHTTPRequestHandler
import socketserver
class CGIServer:
    def __init__(self, port, address, dir):
        self.port = port
        self.addr = address
        self.dir = dir

    def runserver(self):
        port = self.port
        addr = self.addr
        dir = self.dir

        class Handler(CGIHTTPRequestHandler):
            cgi_directories = ["cgi-bin"]
        print(type(port))
        httpd = HTTPServer((addr, port), Handler)
        httpd.serve_forever()
