#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

port = 8080
ip = '127.0.0.1'

def main():
    try:
        os.chdir('/')
        serveur = HTTPServer((ip, port), SimpleHTTPRequestHandler)
        print("Démarrage du serveur HTTP: http://%s:%s" %
              (ip, port))
        serveur.serve_forever()
    except FileNotFoundError as e:
        sys.stderr.write("ERREUR! Le répertoire '%s' n'existe pas!\n" % (repertoire))
        raise e
    except KeyboardInterrupt:
        serveur.socket.close()

if __name__ == '__main__':
    main()
