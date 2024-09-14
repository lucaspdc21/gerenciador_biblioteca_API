from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    # Funções privadas de printar o request recebido (para debug)
    # e de envio de resposta
    def _print_request(self):
        print(self.requestline)
        content_length = int(self.headers['Content-Length'] or 0)
        post_data = self.rfile.read(content_length)
        print(f'Received data: {post_data.decode()}')

    def _send_response(self, status_code, content=None, content_type=None):
        # Status code da resposta
        self.send_response(status_code)
        
        # Os headers do programa
        if content_type != None:
            self.send_header('Content-type', content_type)
        self.end_headers()

        # Retorna o conteúdo da resposta em utf-8
        if content != None:
            self.wfile.write(content.encode("utf-8"))

    
    def do_GET(self):
        self._print_request()


    def do_POST(self):
        self._print_request()


    def do_PUT(self):
        self._print_request()


    def do_DELETE(self):
        self._print_request()
    