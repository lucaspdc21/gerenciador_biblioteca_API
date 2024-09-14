import json
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler
from Controller import BibliotecaController
class RequestHandler(BaseHTTPRequestHandler):
    biblioteca_controller = BibliotecaController()
    # Funções privadas de printar o request recebido (para debug)
    # e de envio de resposta
    def _print_request(self):
        print(self.requestline)
        content_length = int(self.headers['Content-Length'] or 0)
        post_data = self.rfile.read(content_length)
        print(f'Received data: {post_data.decode()}')
        return post_data  # Retorna os dados lidos

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
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/livros':
            livros = self.biblioteca_controller.listar_livros()
            self._send_response(200, json.dumps(livros), 'application/json')
        else:
            self._send_response(404, 'Not Found', 'text/plain')


    def do_POST(self):
        post_data = self._print_request()
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/livros':
            try:
                livro_dados = json.loads(post_data.decode('utf-8'))
                titulo = livro_dados.get('titulo')
                genero = livro_dados.get('genero')
                ano = livro_dados.get('ano')
                #autor_id = livro_dados.get('autor_id')
                if titulo:
                    self.biblioteca_controller.criar_livro(titulo, genero, ano)
                    self._send_response(201, 'Livro criado com sucesso', 'text/plain')
                else:
                    self._send_response(400, 'Título é obrigatório', 'text/plain')
            except json.JSONDecodeError:
                self._send_response(400, 'Dados inválidos', 'text/plain')
        else:
            self._send_response(404, 'Not Found', 'text/plain')



    def do_PUT(self):
        self._print_request()


    def do_DELETE(self):
        self._print_request()
    