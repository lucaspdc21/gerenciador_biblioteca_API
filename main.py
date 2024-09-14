from http.server import HTTPServer
from requestHandler import RequestHandler

def rodar_servidor(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Start...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Servidor interrompido")
        httpd.server_close()

if __name__ == '__main__':
    rodar_servidor()