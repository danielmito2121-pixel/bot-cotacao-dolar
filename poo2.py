class Pessoa:
    def __init__(self, nome, profissao, idade):
      self.nome = nome
      self.profissao = profissao
      self.idade = idade

    def aniversario(self, ano=1):
       self.idade += ano

class PessoaJuridica(Pessoa):
   def __init__(self, nome, profissao, idade):
      super().__init__(nome, profissao, idade)
      self.empresas = [] 

    def empresas():
      return self._empresas
   

pessoa01 = Pessoa('Daniel', 'programador', 18)
pessoa02 = Pessoa('Jorge', 'medico', 20)
pessoa03 = PessoaJuridica('Arthur', 'professor', 30)


