import json
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler
from controller import LibraryController

class RequestParser(BaseHTTPRequestHandler):
    library_controller = LibraryController()
    # Funções privadas
    # Printa o request recebido (para debug)
    def _print_request(self):
        print(self.requestline)
        data = self._get_data()
        print(f'Received data: {data.decode()}')

    # Wrapper da obtenção dos dados de um request
    def _get_data(self) -> None:
        content_length = int(self.headers["Content-Length"] or 0)
        return self.rfile.read(content_length)

    # Wrapper do envio de respostas
    def _send_response(self, status_code: str, content: str = None, content_type: str = None) -> None:
        # Status code da resposta
        self.send_response(status_code)
        
        # Os headers do programa
        if content_type != None:
            self.send_header("Content-type", content_type)
        self.end_headers()

        # Manda o conteúdo da resposta em utf-8
        if content != None:
            self.wfile.write(content.encode("utf-8"))

    
    # Handlers de GET, POST, PUT e DELETE
    # Handler de requests GET
    def do_GET(self) -> None:
        parsed_path = urlparse(self.path).path.strip("/")
        if parsed_path == "books":
            books = self.library_controller.list_books()
            self._send_response(200, json.dumps(books), "application/json")
        else:
            self._send_response(404, "Not Found", "text/plain")

    # Handler de requests POST
    def do_POST(self) -> None:
        data = self._get_data()
        parsed_path = urlparse(self.path).path.strip("/")
        if parsed_path == "books":
            try:
                book_data = json.loads(data.decode("utf-8"))
                if book_data.get("title") != None:
                    self.library_controller.create_book(book_data)
                    self._send_response(201, "Livro criado com sucesso")
                else:
                    self._send_response(400, "Título é obrigatório")
            except json.JSONDecodeError:
                self._send_response(400, "Dados inválidos")
        else:
            self._send_response(404, "Not Found")


    # Handler de requests PUT
    def do_PUT(self) -> None:
        self._print_request()
        self._send_response(501) # Not Implemented

    # Handler de requests DELETE
    def do_DELETE(self) -> None:
        self._print_request()
        self._send_response(501) # Not Implemented