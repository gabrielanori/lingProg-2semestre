class Reptil():

    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return'{} ainda não atingiu maturidade sexual'.format(self.nome)

class Mamifero():

    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1 :
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)

class Camaleao(Reptil):

    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)

class Cavalo(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina
    
    def galopar(self):       
        return '{} galopando'.format(self.nome)
    
    def relinchar(self):
        return '{} relinchando'.format(self.nome)

class Cobra(Reptil):

    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return '{} rastejando'.format(self.nome)

    def trocar_de_pele(self):
        return '{} trocando de pele'.format(self.nome)

class Cachorro(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca

    def latir(self):
        return '{} latindo'.format(self.nome)

    def rosnar(self):
        return '{} rosnando'.format(self.nome)

class Jacare(Reptil):

    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)

    def dormir(self):
        return '{} dormindo'.format(self.nome)

class Gato(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata, vidas):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = vidas

    def miar(self):
        return '{} miando'.format(self.nome)

    def morrer(self):
        if self.vidas > 0 and self.vidas <= 7:
           self.vidas -= 1
           return '{} tem {} vidas sobrando'.format(self.nome, self.vidas)            
        else:
            self.vidas == 0
            return '{} morreu'.format(self.nome)


Camufla = Camaleao("Disfarce", "green", 6, "Grilo")
print(Camufla.mudar_de_cor())
print(Camufla.comer_inseto())

Wildfire = Cavalo("Cavalo de Fogo", "Roxa",10, 4, "Vermelho")
print(Wildfire.galopar())
print(Wildfire.relinchar())

Cascavel = Cobra("Orochimaru", "Vinho", 10, "Mortal")
print(Cascavel.rastejar())
print(Cascavel.trocar_de_pele())

Pastor = Cachorro("Alemão", "Marrom", 8, 4, "Pastor Alemão")
print(Pastor.latir())
print(Pastor.rosnar()) 

Alligator = Jacare("Cuca", "Verde", 15, 40)
print(Alligator.atacar()) 
print(Alligator.dormir())

Siames = Gato("Garfield", "Amarelo", 5, 4, 6)
print(Siames.miar())
print(Siames.morrer())