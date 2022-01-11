import socket
import urllib.request


def internet_on():
    try:
        urllib.request.urlopen('http://pudim.com.br')
    except (socket.gaierror, urllib.error.URLError):
        print('Não consegui acessar o site Pudim com sucesso!')
    else:
        print('Consegui acessar o site Pudim com sucesso!')


# Programa principal
internet_on()
