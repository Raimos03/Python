'''
Author: Pedro Lima
05-02-2021

ver 1.00
'''

import clipboard

def validatel(tel):

    if tel.isnumeric():

        if ' ' not in tel:

            return True
    return False


def validatexto(t):

    if len(t) >= 3:

        lt = [" ", ".", "?", "!"]
        i = 0
        for el in lt:

            if el in t:
                i += 1

        if i >= 1:
            return True

        return False


def criatexto(textoi):

    f = textoi.replace(" ", '%20')
    return f


def criacodigo(inicio, tel, text):

    parte1 = inicio+'55'+tel+'&text='
    parte2 = criatexto(text)
    return parte1+parte2

i = True

while i == True:
    itx = True

    inicio = 'https://api.whatsapp.com/send?phone='

    it = False
    while (it == False):
        tel = input(
            '1- Digite o numero do telefone com DDD no formato: 21985241554. (Digite 2 para sair)\n')

        if tel == str(2):
            itx = False
            vtx = False
            vtel = False
            break

        vtel = validatel(tel)
        # print('ok')

        if vtel == False:
            print('***** Erro de digitação ******')
        else:
            print('***** Telefone Validado *****')
            break

        it = int(input('2-Digite 1 para continuar e 2 para sair\n '))
        if it == 2:

            break
        else:
            it = False

    while itx == True:
        vtx = True

        text = input("3-Digite o texto:(2 para sair) \n")
        if text == str(2):
            vtext=False
            vtx = False
            break

        vtext = validatexto(text)

        while vtx == True:

            print("4-Confirma o texto? \n")
            print('************\t', text, '\t *************\n')
            ct = input("5- 1 para SIM e 2 para NÃO\n")
            if ct == str(1):
                break
            else:

                vtx = False

        if vtext == False:
            print('***** O texto possui erro *****')

        elif vtx == False:
            print('***** O texto nao foi validado *****')
        else:
            print('***** Texto validado *****')
            break

        itx = int(input('2-Digite 1 para continuar e 2 para sair\n '))
        if itx == 2:
            break
        else:
            it = False

    if (vtel == True) and (vtext == True) and (vtx == True):

        mens_final = criacodigo(inicio, tel, text)

        print("***** Pronto. Gerando o link *****")
        clipboard.copy(mens_final)

        print("***** Mensagem copiada para área de transferência. Cole-a no destino*****\n")

    else:

        print("Não foi possivel concluir a mensagem. Tente novamente.\n")

    c = int(input('Deseja continuar mais uma vez? "1" para SIM, "2" para NAO\n'))

    if c == 1:
        i = True

    else:
        i = False
