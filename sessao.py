#Sessão
#Atributos: filme, sala, horário, data, ingressosDisponíveis.
#Métodos: criarSessão(), atualizarSessão(), cancelarSessão().

from filme import Filme
from sala import Sala
from datetime import time

class Sessao:

    sessoes_db = []

    def __init__(self, filme: Filme, sala: Sala, horario: time, ingressos_disponiveis):
        self.__filme = filme
        self.__sala = sala
        self.__horario = time
        self.__ingressos_disponiveis = ingressos_disponiveis

    @property
    def filme(self) -> Filme:
        return self.__filme

    @filme.setter
    def filme(self, filme: filme):
        self.__filme = filme

    @property
    def sala(self) -> Sala:
        return self.__sala

    @sala.setter
    def sala(self, sala: Sala):
        self.__sala = sala
    
    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario: str):
        self.__horario = horario


    def adicionarSessao(self):
        # Adiciona a sessao ao "banco de dados"
        Sessao.sessoes_db.append(self)
        return f"Sessao da sala:'{self.__sala} 'às'{self.__horario} 'adicionada com sucesso."

    def atualizarSessao(self, filme=None, sala=None, data=None, ingressos_disponiveis=None):
        # Atualiza os atributos da sessao se os novos valores forem fornecidos
        if filme is not None:
            self.__filme = filme
        if sala is not None:
            self.__sala = sala
        if horario is not None:
            self.__horario = horario
        if ingressos_diponiveis is not None:
            self.__ingressos_disponiveis = ingressos_diponiveis
        return f"Sessao atualizada: {self.__filme}, {self.__sala}, {self.__horario}, {self.__ingresso_disponiveis}"

    def removerSessao(self):
        # Cancela a sessao do "banco de dados"
        if self in Sessao.sessoes_db:
            Sessao.sessoes_db.remove(self)
            return f"Sessao da sala:'{self.__sala}'às'{self.__horario} 'removida com sucesso."
        else:
            return f"Sessão do filme '{self.__filme}' não encontrada."

    def __str__(self):
        return (f"Filme: {self.__filme}\n"
                f"Sala: {self.__sala}\n"
                f"Horário: {self.__horario}\n"
                f"ingressos_disponiveis: {self.__ingressos_disponiveis}\n")


    def infoSessoes(self):
        for sessao in sessoes_db:
            print(f"Filme: {sessao.filme.titulo}, Sala: {sessao.sala.tipo}, Horário: {sessao.horario}, Ingressos disponíveis: {sessao.ingressos_disponiveis}")
