import socket  #Biel Steve

def Main():
    #cria o socket do cliente
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #define o endereço e porta do servidor
    destino = ('127.0.0.1', 10000)
    
    #aguarda o usuário digitar uma mensagem
    message = input(" -> (q para sair) ")
    
    
    while True:
        
        # envia a mensagem do usuário para o servidor
        sent = mySocket.sendto(message.encode(), destino)
        
        # recebe a devolução da mensagem do servidor
        data, server = mySocket.recvfrom(4096)
        print('Server data: {}: {}'.format(server, data.decode()))
        
        #aguarda nova mensagem do usuário
        message = input(" -> -> (q para sair)  ")

        if (message == 'q'):
            sent = mySocket.sendto(message.encode(), destino)
            break

    mySocket.close()

if __name__ == '__main__':
    Main()