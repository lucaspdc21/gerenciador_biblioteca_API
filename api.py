from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPIHandler(BaseHTTPRequestHandler):

    # Método privado para setar os headers da resposta
    # O status é definido na chamada e contentType é por padrão JSON
    # 200 ok , 201 created, 400 bad request, 404 not found
    def _headers(self, status_code, content_type="application/json"):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    # Simular livros
    livros = {
        "l1": {"id": 1, "nome": "Livro 1"},
        "l2": {"id": 2, "nome": "Livro 2"},
    }

    def do_GET(self):
        path_parts = urlparse(self.path).path.strip("/").split("/")

        if len(path_parts) > 0:
            if path_parts[0] == "items":
                BooksController(self).handle_get(path_parts)
            #elif path_parts[0] == "books":
                #BooksController(self).handle_get(path_parts)
            else:
                self.send_error(404, "Not Found")
        else:
            self.send_error(404, "Not Found")


def rodar_servidor(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
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
