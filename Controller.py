from Autor import Autor
from Livro import Livro


class BibliotecaController:
    def __init__(self):
        self.livros = {}
        self.autores = {}
        self.livro_id_counter = 1
        self.autor_id_counter = 1

    def criar_livro(self, titulo, genero=None, ano=None, autor_id=None):
        livro = Livro(self.livro_id_counter, titulo, genero, ano, autor_id)
        self.livros[self.livro_id_counter] = livro
        self.livro_id_counter += 1

    def listar_livros(self):
        return [livro.get_dados() for livro in self.livros.values()]

    def buscar_livro(self, id):
        return self.livros.get(id)

    def atualizar_livro(self, id, dados):
        livro = self.livros.get(id)
        if livro:
            livro.titulo = dados.get('titulo', livro.titulo)
            livro.genero = dados.get('genero', livro.genero)
            livro.ano = dados.get('ano', livro.ano)
            return True
        return False

    def excluir_livro(self, id):
        return self.livros.pop(id, None)
