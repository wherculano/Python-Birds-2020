class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}. Meu ID é {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'


class Homem(Pessoa):
    """Classe que herda todos os atributos e metodos da classe Pessoa"""
    def cumprimentar(self):
        # sobrescrita do método de classe
        return f'{super().cumprimentar()}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 1  # sobrescrita de atributo de classe


if __name__ == '__main__':
    wagner = Homem(nome='Wagner')
    herculano = Pessoa(wagner, nome='Herculano')
    print(Pessoa.cumprimentar(wagner))
    print(f'ID: {id(wagner)}')
    print(wagner.nome)
    print(wagner.cumprimentar())
    print(wagner.idade)
    for filho in herculano.filhos:
        print(filho.nome)
    wagner.sobrenome = 'Santos'  # Criado atributo dinamicamente
    print(wagner.sobrenome)
    print(id(Pessoa.olhos), id(wagner.olhos), id(herculano.olhos))  # verificando id dos atributos de classe
    wagner.olhos = 3  # criando atributo dinamico
    print(Pessoa.olhos, wagner.olhos, herculano.olhos)  # verificando atributos de classe/instancia
    print(wagner.__dict__)
    print(herculano.__dict__)
    del wagner.sobrenome  # Excluindo atributo dinamicamente
    del wagner.olhos  # Excluindo atributo de instancia para voltar ao valor do atributo de classe
    print(wagner.__dict__)
    print(Pessoa.olhos, wagner.olhos, herculano.olhos)
    print(Pessoa.nome_e_atributos_de_classe(), wagner.nome_e_atributos_de_classe())
    # Verificando se herculano e wagner são do tipo Pessoa e do tipo Homem
    print(isinstance(herculano, Pessoa), isinstance(herculano, Homem))
    print(isinstance(wagner, Pessoa), isinstance(wagner, Homem))
    ciclope = Mutante(nome='Ciclope')
    print(ciclope.olhos)
    print(wagner.cumprimentar())
    print(herculano.cumprimentar())
