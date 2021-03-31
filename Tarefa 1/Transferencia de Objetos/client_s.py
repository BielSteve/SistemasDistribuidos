import socket
import threading


def rodaThread(mySocket):
    #Receber mensagens do servidor
    while True:
        # recebe a devolução da mensagem do servidor
        data = mySocket.recv(1024)
        print(data.decode())
        #print('Recebido do servidor {}: {}'.format( mySocket.getpeername(),data.decode()))



def Main():
    
    host = '127.0.0.1'
    port = 10000
    
    #cria o socket do cliente
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #realiza a conexao com o servidor
    mySocket.connect((host,port))
    
    #cria e inicia a thread
    t = threading.Thread(target=rodaThread, args=(mySocket,))
    t.start()
    
    #aqui vai ser para pegar o nome do usuario, to passando a condição no while, enquanto o nome for nulo, vc pode digitar o nome
    nome = None;
    while nome == None:
        nome = input("Digite seu nome: ")
    
    #aqui vamos pegar a mensagem do usuário
    while True:
        #aguarda o usuário digitar uma mensagem
        message = input()
        
        if message == 'q':
            mySocket.send(message.encode())
            break
        
        #colocando nome do usuario e a mensagem dentro da variavel nova e colocando um separador +
        nova = nome +'+'+ message
        
        # envia a mensagem do usuário para o servidor
        mySocket.send(nova.encode())
        
    #fecha conexão com sevidor    
    mySocket.close()
    


if __name__ == '__main__':
    Main()