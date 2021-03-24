import socket
import threading


def rodaThread(mySocket):
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
    
    #aguarda o usuário digitar uma mensagem
    message = input(" -> (q sair) ")
    
    while message != 'q' and message:
        
        # envia a mensagem do usuário para o servidor
        mySocket.send(message.encode())
              
        #aguarda nova mensagem do usuário
        message = input(" -> (q sair) ")
        
        
    mySocket.close()
    
if __name__ == '__main__':
    Main()