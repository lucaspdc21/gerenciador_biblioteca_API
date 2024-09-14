class Livro:
    def __init__(self, id, titulo, genero=None, ano=None, autor_id=None):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.autor_id = autor_id

    def get_dados(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'ano': self.ano,
            'autor_id': self.autor_id
        }
