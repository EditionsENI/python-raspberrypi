#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
port = 8080
ip = '127.0.0.1'

class HTTPi(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text-html; charset=UTF-8")
        self.end_headers()
        content = """
<html>
<head>
<title>Hello Pi!</title>
</head>
<body>
  <h1>Hello Pi!</h1>
</body>
</html>"""
        body = content.encode('UTF-8')
        self.wfile.write(body)

def main():
    try:
        serveur = HTTPServer((ip, port), HTTPi)
        print("Démarrage du serveur HTTPi: http://%s:%s" %
              (ip, port))
        serveur.serve_forever()
    except KeyboardInterrupt:
        serveur.socket.close()

if __name__ == '__main__':
    main()
