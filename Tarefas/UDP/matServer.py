import socket #Biel Steve
import re


def Main():
    host = "127.0.0.1"
    port = 10000
    # cria o socket UDP do servidor (Internet,Transporte)
    socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Configura o IP e a porta que o servidor vai ficar executando
    
    socketUDP.bind((host,port))
    a = ' - Abc Bolinhas'
    print(a)
    
    print('Servidor UDP: {}:{}'.format(host,port))

    while True:

        print('Esperando mensagens...')
        data, address = socketUDP.recvfrom(4096) # buffer size - bytes
        print('Recebido {} bytes de {}'.format(len(data), address))
        
        #Transformando data em str e criando variavel novo
        novo = data.decode()
        print(novo)
        
        # metodo find procura na string
        soma = novo.find('+')
        menos = novo.find('-')
        div = novo.find('/')
        vezes = novo.find('*')
        mod = novo.find('%')
        
        
        #separar operadores dos numeros
        valor = re.split('\+|-|\%|\*|\/|\n', novo)
        
        print(valor[0])
        print(valor[1])
        
        #verificando qual operador é, fazendo o calculo e ja enviando para o Client
        if soma > 0:
            resul = int(valor[0]) + int(valor[1])
            sent = socketUDP.sendto(str(resul).encode(), address)
        elif menos > 0:
            resul = int(valor[0]) - int(valor[1])
            sent = socketUDP.sendto(str(resul).encode(), address)
        elif div > 0:
            resul = int(valor[0]) / int(valor[1])
            sent = socketUDP.sendto(str(resul).encode(), address)
        elif vezes > 0:
            resul = int(valor[0]) * int(valor[1])
            sent = socketUDP.sendto(str(resul).encode(), address)
        elif mod > 0:
            resul = int(valor[0]) % int(valor[1])
            sent = socketUDP.sendto(str(resul).encode(), address) 
        else:
            print('Tem alguma coisa errada ai parça')
      


    socketUDP.close()

if __name__ == '__main__':
    Main()