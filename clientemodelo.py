class ClienteModelo:
  """
    Classe que representa o modelo de um Cliente.

    Atributos:
    - nome
    - fone
    - email
  """
clientes_db = []

    def __init__(self, nome: str, fone: str, email: str):
        self.__nome = nome
        self.__fone = fone
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        self.__fone = fone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email
