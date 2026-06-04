class Pessoa:
    def __init__(self, nome, profissao, idade):
      self.nome = nome
      self.profissao = profissao
      self.idade = idade

    def aniversario(self, ano=1):
       self.idade += ano

pessoa01 = Pessoa('Daniel', 'programador', 18)
pessoa02 = Pessoa('Jorge', 'medico', 20)

print(pessoa01.nome)
print(pessoa02.profissao)

print(f"Idade esse ano: {pessoa01.idade}")
pessoa01.aniversario(5)
print(f"Idade em 5 anos: {pessoa01.idade}")

