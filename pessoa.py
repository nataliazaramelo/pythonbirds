class Pessoa:
    olhos = 2 #atributo de classe/default usado quando todos os objetos compartilham do mesmo valor

    def __init__(self, *filhos, nome=None, idade=34): #metodo especial para criar o atributo de um objeto - valor nulo = None, nome é um atributo
        self.nome = nome # atributo de dado, atributos de instancia e objeto são criados pelo metodo __init__
        self.idade = idade # atributos de uma instância podem ser compostos de qualquer objeto
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    natalia = Pessoa(nome='Natalia') #objeto complexo do tipo pessoa tem nome e está sendo passado como atributo para objeto junior
    junior = Pessoa(natalia, nome='Junior') #natalia seria filho de junior
    print(Pessoa.cumprimentar(natalia));
    print(id(natalia))
    print(natalia.cumprimentar())
    print(natalia.nome)
    print(natalia.idade)
    print(junior.nome)
    print(junior.idade)
    print(natalia.olhos)
    print(junior.olhos)
    print(id(Pessoa.olhos), id(junior.olhos), id(natalia.olhos))
    natalia.nome = 'Natália' #altera o objeto
    #print(natalia.nome)
    #print(natalia.idade)
    for filho in junior.filhos:#criando um atributo complexo
        print(junior .filhos)
        natalia.sobrenome = 'Zaramelo'# incluindo atributo dinâmico, atributos dinâmicos não são recomendados.
        # del natalia.filhos deletando atributo dinânmico
        natalia.olhos = 1 # aqui está sendo inserido um atributo no objeto
        print(natalia.__dict__)#__dict__possui referencia apenas para os atributo de instância, portanto quando você insere o atributo no objeto ele passa a fazer parte do objeto
        print(junior.__dict__)
        print(id(Pessoa.olhos), id(junior.olhos), id(natalia.olhos))
