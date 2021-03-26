import socket
import threading


def rodaThread(mySocket):
    
    while True:
        # recebe a devolução da mensagem do servidor
        data = mySocket.recv(1024)
        
        print('Recebido do servidor {}: {}'.format( mySocket.getpeername(),data.decode()))



def Main():
    
    host = '127.0.0.1'
    port = 10000
    
    #cria o socket do cliente
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #realiza a conexao com o servidor
    mySocket.connect((host,port))
    

    
    t = threading.Thread(target=rodaThread, args=(mySocket,))
    t.start()
    
    while True:
        nome = input("Digite seu nome: ")
        #aguarda o usuário digitar uma mensagem
        message = input("Digite sua mensagem:")
        nova = nome.encode()+message.encode()
        
        # envia a mensagem do usuário para o servidor
        mySocket.send(message.encode())
        
        
    mySocket.close()
    


if __name__ == '__main__':
    Main()