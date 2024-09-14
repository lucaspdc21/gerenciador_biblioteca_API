from http.server import BaseHTTPRequestHandler
import identidades
import json

class RequestHandler(BaseHTTPRequestHandler):
    # Funções privadas
    # Printa o request recebido (para debug)
    def _print_request(self):
        print(self.requestline)
        content_length = int(self.headers['Content-Length'] or 0)
        post_data = self.rfile.read(content_length)
        print(f'Received data: {post_data.decode()}')

    # Wrapper de enviar resposta
    def _send_response(self, status_code: int, status_message: str = None, content: str = None, content_type: str = None):
        # Status code da resposta
        self.send_response(status_code, status_message)
        
        # Os headers do programa
        if content_type != None:
            self.send_header('Content-type', content_type)
        self.end_headers()

        # Retorna o conteúdo da resposta em utf-8
        if content != None:
            self.wfile.write(content.encode("utf-8"))

    # Função para serializar objetos customizados
    def _serializeObj(self, obj) -> dict:
        if getattr(obj, "to_dict") != None:
            return obj.to_dict()
        else:
            raise TypeError(f"Não foi possível serializar o objeto de tipo {obj.__class__.__name__}.")


    # Handler de requests GET
    def do_GET(self):
        path = self.path.strip("/")
        response_data = None
        
        #TODO: ligar com o controller

        if response_data == None:
            self._send_response(404)
        else:
            response_data = json.dumps(response_data, default=self._serializeObj)
            self._send_response(200, content=response_data, content_type="application/json")
        
    # Handler de requests POST
    def do_POST(self):
        self._print_request()

    # Handler de requests PUT
    def do_PUT(self):
        self._print_request()

    # Handler de requests DELETE
    def do_DELETE(self):
        self._print_request()
    