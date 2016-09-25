#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
port = 8080
ip = '127.0.0.1'

class HTTPi(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text-html; charset=UTF-8")
        self.end_headers()
        try:
            with open('index.html', 'r', encoding='UTF-8') as index:
                body = ''.join(index.readlines()).encode('UTF-8')
        except FileNotFoundError:
            body = "<h1>Le fichier index.html n'existe pas!<h1>".encode('UTF-8')
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
