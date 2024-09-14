class Autor:
    def __init__(self, id, nome, data_nascimento=None, nacionalidade=None):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade

    def get_dados(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento,
            'nacionalidade': self.nacionalidade
        }
