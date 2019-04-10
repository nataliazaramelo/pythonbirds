class Pessoa:
    def __init__(self, nome=None, idade=34): #metodo especial para criar o atributo de um objeto - valor nulo = None, nome é um atributo
        self.nome = nome # atributo de dado, atributos de instancia e objeto são criados pelo metodo __init__
        self.idade = idade
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Natalia') #objeto
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Natália' #altera o objeto
    print(p.nome)
    print(p.idade)
