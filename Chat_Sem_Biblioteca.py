import os
from threading import main_thread

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} Sim, na minha opinião aprender python é fundamental, pois ele é flexivel e pode ser usado em vários lugares.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} Com certeza quando você estiver programando em Python logo arrumará um emprego{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} Isso é muito particular, vai depender de quanto tempo você se dedicara aos estudos, quanto mais estudar, menos tempo para ficar BOM{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} Em um curso bala para aprender Python{os.linesep}')
    else:
        print("Digite apnas 1,2,3 ou 4\n")

def start():
    # Apresentar o chatbot
    print('Olé bem vindo ao meu chat de duvidas especificas:')
    # pedir o nome
    nome = input('Informe seu nome:\n')
    # pedir o e-mail
    email = input('Informe seu email:\n')
    while True:
        # Oferecer o menu de opções
        resposta = input(f'O que gostaria de saber?{os.linesep}[1] - Vale a pena aprender Python?{os.linesep}[2] - Quanto tempo leva para conseguir um emprego com Python?{os.linesep}[3] - Quando vou saber se estou BOM o suficiente para conseguir um emprego?{os.linesep}[4] - Onde recomenda estudar Python?{os.linesep}')
        #Processar a resposta enviada
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
