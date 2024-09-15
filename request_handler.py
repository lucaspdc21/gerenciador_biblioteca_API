import json
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler
from request_adapter import RequestAdapter

class RequestHandler(BaseHTTPRequestHandler):
    request_adapter = RequestAdapter()
    
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
    def _send_response(self, status_code: int, content: str = None, content_type: str = None, status_message: str = None,) -> None:
        # Status code da resposta
        self.send_response(status_code, status_message)
        
        # Os headers do programa
        if content_type is not None:
            self.send_header("Content-type", content_type)
        self.end_headers()

        # Manda o conteúdo da resposta em utf-8
        if content is not None:
            self.wfile.write(content.encode("utf-8"))

    
    # Handlers de GET, POST, PUT e DELETE
    # Handler de requests GET
    def do_GET(self) -> None:
        # pega os dados do request
        data = self._get_data()
        parsed_path = urlparse(self.path).path.strip("/").split("/")
        
        # obtém a resposta
        response = self.request_adapter.get(parsed_path, data)
        
        # envia a resposta pro cliente
        self._send_response(response.get("status_code"), response.get("content"), 
                            response.get("content_type"), response.get("status_message"))

    # Handler de requests POST
    def do_POST(self) -> None:
        data = self._get_data()
        parsed_path = urlparse(self.path).path.strip("/").split("/")
        
        response = None
        if self.headers.get("Content-Type") != "application/json":
            response = {"status_code": 415, "status_message": "Este servidor só aceita JSON."}
        else:
            try:
                data = json.loads(data)
                response = self.request_adapter.post(parsed_path, data)
            except json.JSONDecodeError:
                response = {"status_code": 415}
            except:
                response = {"status_code": 500}
        

        self._send_response(response.get("status_code"), response.get("content"), 
                            response.get("content_type"), response.get("status_message"))


    # Handler de requests PUT
    def do_PUT(self) -> None:
        self._print_request()
        self._send_response(501) # Not Implemented

    # Handler de requests DELETE
    def do_DELETE(self) -> None:
        self._print_request()
        self._send_response(501) # Not Implemented