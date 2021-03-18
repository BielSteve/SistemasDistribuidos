import socket #Biel Steve
import re
import math

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
        
        novo = str(data, 'utf-8')
        print(novo)
        
        operador = re.search('\+|-|\%|\*|\/|\n', novo)
        valor = re.split('\+|-|\%|\*|\/|\n', novo)
        
        if (valor[0].isdigit() and valor[1].isdigit()):
            if(operador[0] == '-'):
                resul = float(valor[0]) - float(valor[1])
            elif(operador[0] == '+'):
                resul = float(valor[0]) + float(valor[1])
            elif(operador[0] == '*'):
                resul = float(valor[0]) * float(valor[1])
            elif(operador[0] == '/'):
                resul = float(valor[0]) / float(valor[1])
            elif(operador[0] == '%'):
                resul = math.fmod(float(valor[0]), float(valor[1]))  
            else:
                print('Tem alguma coisa errada ai parça')
            if (resul):                    
                sent = socketUDP.sendto(str(resul).encode('utf-8'), address)       


    socketUDP.close()

if __name__ == '__main__':
    Main()