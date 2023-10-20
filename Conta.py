class Conta:
    def __init__(self, _titular, numero, saldo):
        self.saldo= saldo
        self.numero=numero
        self.titular=_titular
    
        ######################################################################################################
        #A função Property é um Decorator e é utilizada para obter um valor de um atributo.
        #Basicamente, a função Property permite que você declare uma função para obter o valor de um atributo.
        #Importante
        #Em Python, não é considerada uma boa prática criar uma classe e, logo em seguida, adicionar propriedades (property) para todos os atributos.
        #A função Property deve ser utilizada somente se você precisar da funcionalidade de transformar ou verificar um atributo quando ele é atribuído ou lido.
        ######################################################################################################

        #print(self.titular)

        @property
        def saldo(self):
            return self._saldo
        
        @saldo.setter
        def saldo(self, saldo):
            if (saldo < 0):
                print('O Saldo não pode ser negativo')
            else:
                self._saldo = saldo

    def deposita(self, valor):
        self.saldo=+valor

    def saque(self, valor):
        self.saldo=-valor
 
    def extrato(self):
        print("Cliente: ", self.titular, " Saldo Atual: ",self.saldo)
