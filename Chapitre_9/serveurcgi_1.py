#!/usr/bin/env python3
from http.server import CGIHTTPRequestHandler, HTTPServer
import os, sys
port = 8080
ip = '127.0.0.1'
repertoire = '/home/pi/www'

def main():
    try:
        os.chdir(repertoire)
        serveur = HTTPServer((ip, port), CGIHTTPRequestHandler)
        print("Démarrage du serveur CGI: http://%s:%s" %
              (ip, port))
        serveur.serve_forever()
    except FileNotFoundError as e:
        sys.stderr.write("ERREUR! Le répertoire '%s' n'existe pas!\n" % (repertoire))
        raise e
    except KeyboardInterrupt:
        serveur.socket.close()

if __name__ == '__main__':
    main()
