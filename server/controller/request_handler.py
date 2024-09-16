import json
import traceback
import re
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler
from controller.request_adapter import RequestAdapter

class RequestHandler(BaseHTTPRequestHandler):
    request_adapter = RequestAdapter()
    
    # Funções privadas
    # Printa o request recebido (para debug)
    def _print_request(self):
        print(self.requestline)
        data = self._get_data()
        print(f'Received data: {data.decode()}')

    # Função que lida com requests OPTIONS (fornt-end)
    def do_OPTIONS(self) -> None:
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    # Wrapper da obtenção dos dados de um request
    def _get_data(self) -> None:
        content_length = int(self.headers["Content-Length"] or 0)
        return self.rfile.read(content_length)

    # Wrapper do envio de respostas
    def _send_response(self, response: dict) -> None:
        # Status code da resposta
        status_code = response.get("status_code")
        status_message = response.get("status_message")
        if status_message is not None:
            status_message = status_message.encode("utf-8")
        self.send_response(status_code, status_message)
        
        # Os headers do programa
        headers = response.get("headers", {})
        for key, value in headers.items():
            self.send_header(key, value)

        # Headers de CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

        # Manda o conteúdo da resposta em utf-8
        content = response.get("content")
        if content is not None:
            self.wfile.write(content.encode("utf-8"))

    
    # Handlers de GET, POST, PUT e DELETE
    # Handler de requests GET
    def do_GET(self) -> None:
        # pega os dados do request
        parsed_path = re.sub("/+", "/", urlparse(self.path).path.strip("/")).split("/")
        print(parsed_path)
        
        # obtém a resposta
        response = self.request_adapter.get(parsed_path)
        
        # envia a resposta pro cliente
        self._send_response(response)

    # Handler de requests POST
    def do_POST(self) -> None:
        data = self._get_data()
        parsed_path = re.sub("/+", "/", urlparse(self.path).path.strip("/")).split("/")
        
        response = None
        content_type = self.headers.get("Content-Type")
        if content_type not in ("application/json", None):
            response = {
                "status_code": 415,
                "headers": {
                    "Accept-Post": "application/json; charset=UTF-8"
                }
            }
        else:
            try:
                if content_type is None:
                    data = {}
                else:
                    data = json.loads(data)
                response = self.request_adapter.post(parsed_path, data)
            except json.JSONDecodeError:
                response = {
                    "status_code": 415,
                    "headers": {
                        "Accept-Post": "application/json; charset=UTF-8"
                    }
                }
            except Exception as e:
                print(e)
                response = {"status_code": 500}
                traceback.print_exc()
        

        self._send_response(response)


    # Handler de requests PUT
    def do_PUT(self) -> None:
        data = self._get_data()
        parsed_path = re.sub("/+", "/", urlparse(self.path).path.strip("/")).split("/")
        
        response = None
        if self.headers.get("Content-Type") != "application/json":
            response = {
                "status_code": 415,
                "headers": {
                    "Accept-Post": "application/json; charset=UTF-8"
                }
            }
        else:
            try:
                data = json.loads(data)
                response = self.request_adapter.put(parsed_path, data)
            except json.JSONDecodeError:
                response = {
                    "status_code": 415,
                    "headers": {
                        "Accept-Post": "application/json; charset=UTF-8"
                    }
                }
            except:
                response = {"status_code": 500}
        

        self._send_response(response)

    # Handler de requests DELETE
    def do_DELETE(self) -> None:
        parsed_path = re.sub("/+", "/", urlparse(self.path).path.strip("/")).split("/")
        
        # obtém a resposta
        response = self.request_adapter.delete(parsed_path)
        
        # envia a resposta pro cliente
        self._send_response(response)