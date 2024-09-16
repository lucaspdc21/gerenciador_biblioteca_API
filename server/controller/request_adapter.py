import json
from controller.controller import LibraryController
# TODO: mover as mensagens de erro do status_message pra um content. do jeito que tá é bem paia.

class RequestAdapter():
    def __init__(self):
        self.controller: LibraryController = LibraryController()

    # Validação do dict de um livro (title = str, genre = str, year = int, author_id = str)
    def validate_book(self, data: dict) -> dict:
        title = data.get("title")
        genre = data.get("genre")
        year = data.get("year")
        author_id = data.get("author_id")

        if type(title) != str or title is None:
            return {
                "status_code": 400,
                "headers": {"Content-Type": "application/json"},
                "content": "{\"error\": \"Título é obrigatório e deve ser uma string.\"}",
            }
        if type(genre) != str and genre is not None:
            return {
                "status_code": 400,
                "headers": {"Content-Type": "application/json"},
                "content": "{\"error\": \"Gênero deve ser uma string.\"}",
            }
        if type(year) != int and year is not None:
            return {
                "status_code": 400,
                "headers": {"Content-Type": "application/json"},
                "content": "{\"error\": \"Ano deve ser um número inteiro.\"}",
            }
        if author_id is not None:
            if type(author_id) != str:
                return {
                    "status_code": 400,
                    "headers": {"Content-Type": "application/json"},
                    "content": "{\"error\": \"author_id deve ser uma string.\"}",
                }
            elif self.controller.get_author(author_id) is None: # Deve existir um autor com o ID
                return {
                    "status_code": 400,
                    "headers": {"Content-Type": "application/json"},
                    "content": "{\"error\": \"Não existe um autor com o id solicitado.\"}",
                }
        
        return {"status_code": 200}
    
    # Validação do dict de um autor (name = str, birthday = int, nationality = str)
    def validate_author(self, data: dict) -> dict:
        name = data.get("name")
        birthday = data.get("birthday")
        nationality = data.get("nationality")

        if type(name) != str or name is None:
            return {
                "status_code": 400,
                "headers": {"Content-Type": "application/json"},
                "content": "{\"error\": \"Nome é obrigatório e deve ser uma string.\"}",
            }
        if type(birthday) != int and birthday is not None:
            return {
                "status_code": 400,
                "headers": {"Content-Type": "application/json"},
                "content": "{\"error\": \"Data de nascimento deve ser um número inteiro.\"}",
            }
        if type(nationality) != str and nationality is not None:
            return {
                "status_code": 400,
                "headers": {"Content-Type": "application/json"},
                "content": "{\"error\": \"Nacionalidade deve ser uma string.\"}",
            }
        
        return {"status_code": 200}


    # requests GET (GET /, GET /books, GET /author, GET /books/{id}, GET /author/{id}, GET /author/{id}/books)
    def get(self, path: list, data: any = None) -> dict:
        match (path[0], len(path)):
            # Pasta raíz
            case ("", 1): # GET / -- pasta raíz, todos os livros e todos os autores
                return {
                    "status_code": 200,
                    "headers": {"Content-Type": "application/json"},
                    "content": json.dumps(self.controller.list_root()),
                }
            
            # Livros
            case ("books", 1): # GET /books -- todos os livros
                return {
                    "status_code": 200,
                    "headers": {"Content-Type": "application/json"},
                    "content": json.dumps(self.controller.list_books()),
                }    
            case ("books", 2): # GET /books/{id} -- livro específico
                book = self.controller.get_book(path[1])
                if book is not None:
                    return {
                        "status_code": 200,
                        "headers": {"Content-Type": "application/json"},
                        "content": json.dumps(book),
                    }
                            
            # Autores
            case ("authors", 1): # GET /authors -- todos os autores
                return {
                    "status_code": 200,
                    "headers": {"Content-Type": "application/json"},
                    "content": json.dumps(self.controller.list_authors()),
                }
            case ("authors", 2): # GET /authors/{id} -- autor específico
                author = self.controller.get_author(path[1])
                if author is not None:
                    return {
                        "status_code": 200,
                        "headers": {"Content-Type": "application/json"},
                        "content": json.dumps(author),
                    }
            case ("authors", 3) if path[2] == "books": # GET /authors/{id}/books -- todos os livros de um autor
                author = self.controller.get_author(path[1])
                if author is not None:
                    return {
                        "status_code": 200,
                        "headers": {"Content-Type": "application/json"},
                        "content": json.dumps(self.controller.get_author_books(path[1])),
                    }

        # Retorna 404 Not Found se o request não for encontrado no match case
        return {"status_code": 404}
    

    # requests POST (POST /books, POST /authors, POST /authors/{id}/books/{book_id})
    def post(self, path: list, data: any) -> dict:
        match (path[0], len(path)):
            # Requests post válidos
            case ("books", 1): # POST /books -- cadastrar novo livro
                response = self.validate_book(data)
                if response["status_code"] != 200:
                    return response
                book_id = self.controller.create_book(data)
                response["headers"] = {"Content-Type": "application/json"}
                response["content"] = json.dumps(book_id) # retorna o id assimilado ao livro criado
                return response
            case ("authors", 1): # POST /authors -- cadastrar novo autor
                response = self.validate_author(data)
                if response["status_code"] != 200:
                    return response
                author_id = self.controller.create_author(data)
                response["headers"] = {"Content-Type": "application/json"}
                response["content"] = json.dumps(author_id) # retorna o id assimilado ao autor criado
                return response
            case ("authors", 4): # POST /authors/{id}/books/{book_id} -- linkar autor e livro
                author = self.controller.get_author(path[1])
                book = self.controller.get_book(path[3])
                if author is not None and book is not None:
                    if author["books"].get(path[3]) is None and book.get("author_id") is None:
                        self.controller.create_association(path[1], path[3])
                        return {"status_code": 200}
                    else:
                        return { # já existe o link
                            "status_code": 409,
                            "headers": {"Content-Type": "application/json"},
                            "content": "{\"error\": \"A associação entre autor e livro já existe.\"}"
                        }
                else:
                    return {"status_code": 404} # autor ou livro não existe                    

            # Requests post inválidos
            # POST na pasta raiz
            case ("", 1):
                return {"status_code": 403}
            # POST dentro de um livro, autor, ou livros do autor
            case ("books", 2) | ("authors", 2) | ("authors", 3):
                if self.get(path)["status_code"] == 200:
                    return {"status_code": 403}

        # Retorna 404 Not Found se o alvo do request POST não for encontrado no match case
        return {"status_code": 404}

    def put(self, path: list, data: any) -> dict:
        if path[0] == "":  
            return {"status_code": 403}

        p0 = path[0]
        match (p0, len(path)):
            # Requests PUT válidos
            case ("books", 2):  # PUT /books/{id}
                response = self.validate_book(data)
                if response["status_code"] != 200:
                    return response
                self.controller.update_book(path[1], data)
                return {"status_code": 200}
            case ("authors", 2):  # PUT /authors/{id}
                response = self.validate_author(data)
                if response["status_code"] != 200:
                    return response
                self.controller.update_author(path[1], data)
                return {"status_code": 200}

        # Retorna 404 Not Found se o request não for encontrado no match case
        return {"status_code": 404}


    # requests DELETE (DELETE /books/{id}, DELETE /authors/{id}, DELETE /authors/{id}/books/{book_id})
    def delete(self, path: list, data: any = None) -> dict:            
        match (path[0], len(path)):
            # Requests Deletes válidos
            case("books", 2): # DELETE /books/{id}
                book = self.controller.get_book(path[1])
                if book is not None:
                    self.controller.delete_book(path[1])
                    return {"status_code": 200}
                    
            case("authors", 2): # DELETE /authors/{id}
                author = self.controller.get_author(path[1])
                if author is not None:
                    self.controller.delete_author(path[1])
                    return {"status_code": 200}
            case("authors", 4): # DELETE /authors/{id}/books/{id}
                author = self.controller.get_author(path[1])
                book = self.controller.get_book(path[3])
                if author is not None and book is not None:
                    if author["books"].get(path[3]) is not None and book.get("author_id") is not None:
                        self.controller.delete_association(path[1], path[3])
                        return {"status_code": 200}
                else:
                    return {"status_code": 404} # autor ou livro não existe, ou a associação entre os dois não existe.
                
            # Requests post inválidos
            # DELETE da pasta raiz, books ou authors
            case ("", 1) | ("books", 1) | ("authors", 1):
                return {"status_code": 403}
            # DELETE dentro de um livro, autor, ou livro de autor
            case ("books", 3) | ("authors" , 3) | ("authors", 5):
                path.pop()
                if self.get(path)["status_code"] == 200:
                    return {"status_code": 403}
            
                    
        return {"status_code": 404}
