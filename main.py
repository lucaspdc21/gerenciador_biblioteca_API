from http.server import HTTPServer
from request_parser import RequestParser

def run_server(server_class=HTTPServer, handler_class=RequestParser, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Start...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Servidor interrompido")
        httpd.server_close()

if __name__ == '__main__':
    run_server()