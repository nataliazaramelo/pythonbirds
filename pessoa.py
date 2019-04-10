class Pessoa:
    def __init__(self, *filhos, nome=None, idade=34): #metodo especial para criar o atributo de um objeto - valor nulo = None, nome é um atributo
        self.nome = nome # atributo de dado, atributos de instancia e objeto são criados pelo metodo __init__
        self.idade = idade # atributos de uma instância podem ser compostos de qualquer objeto
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    natalia = Pessoa(nome='Natalia') #objeto complexo do tipo pessoa tem nome e está sendo passado como atributo para objeto junior
    junior = Pessoa(natalia, nome='Junior') #natalia seria filho de junior
    print(Pessoa.cumprimentar(natalia))
    print(id(natalia))
    print(natalia.cumprimentar())
    print(natalia.nome)
    natalia.nome = 'Natália' #altera o objeto
    #print(natalia.nome)
    #print(natalia.idade)
    for filho in natalia.filhos:#criando um atributo complexo
        print(natalia.filhos)
