import http.server
import socketserver
class Httpserver:
    def __init__(self, address, port, dir):
        self.port = port
        self.dir = dir
        self.address = address


    def runserver(self):
        dir = self.dir
        addr = self.address
        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=dir, **kwargs)

        with socketserver.TCPServer((addr, self.port), Handler) as httpd:
            print("Building server", self.port)
            httpd.serve_forever()
            
