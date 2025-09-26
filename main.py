from typing import List, Optional
from datetime import date

class Genero:
    def __init__(self, id_genero: int, nome: str, descricao: str = ""):
        self.id_genero = id_genero
        self.nome = nome
        self.descricao = descricao

class Ator:
    def __init__(self, id_ator: int, nome: str, data_nascimento: date, nacionalidade: str):
        self.id_ator = id_ator
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.filmes: List[Filme] = []
    
    def obter_filmes(self) -> List['Filme']:
        return self.filmes
    
    def adicionar_filme(self, filme: 'Filme'):
        if filme not in self.filmes:
            self.filmes.append(filme)

class Filme:
    def __init__(self, id_filme: int, titulo: str, diretor: str, ano_lancamento: int, 
                 duracao: int, genero: Genero, quantidade_total: int = 1):
        self.id_filme = id_filme
        self.titulo = titulo
        self.diretor = diretor
        self.ano_lancamento = ano_lancamento
        self.duracao = duracao
        self.genero = genero
        self.quantidade_total = quantidade_total
        self.quantidade_estoque = quantidade_total
        self.atores: List[Ator] = []
    
    def verificar_disponibilidade(self) -> bool:
        return self.quantidade_estoque > 0
    
    def adicionar_estoque(self, quantidade: int):
        self.quantidade_estoque += quantidade
        self.quantidade_total += quantidade
    
    def remover_estoque(self, quantidade: int):
        if self.quantidade_estoque >= quantidade:
            self.quantidade_estoque -= quantidade
    
    def obter_atores(self) -> List[Ator]:
        return self.atores
    
    def adicionar_ator(self, ator: Ator, personagem: str = ""):
        if ator not in self.atores:
            self.atores.append(ator)
            ator.adicionar_filme(self)

class Locadora:
    def __init__(self):
        self.filmes: List[Filme] = []
        self.atores: List[Ator] = []
        self.generos: List[Genero] = []
    
    def adicionar_filme(self, filme: Filme):
        self.filmes.append(filme)
    
    def buscar_por_genero(self, genero_nome: str) -> List[Filme]:
        return [filme for filme in self.filmes if filme.genero.nome.lower() == genero_nome.lower()]
    
    def buscar_filmes_disponiveis(self) -> List[Filme]:
        return [filme for filme in self.filmes if filme.verificar_disponibilidade()]