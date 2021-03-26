import socket
import threading

lista = []

def rodaThread(conn):
    while True:
        

        print('Esperando mensagens...')
        data = conn.recv(1024)

        nova = data.decode()
        
        for x in lista:
            if conn != x:
                x.send(nova.encode())
        
        if not data:
            print('Fechando a conexão')
            conn.close()
            break
        
        #Se tiver dados
        print('Recebido {} bytes de {}'.format(len(data), conn.getpeername()))
        # devolve a mensagem para o cliente
        conn.sendall(data)


    conn.close()
    return


def Main():

    host = "0.0.0.0"
    port = 10000
    
    # cria o socket TCP do servidor (Internet,Transporte)
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Configura o IP e a porta que o servidor vai ficar executando
    socketTCP.bind((host,port))
    #Escuta
    socketTCP.listen(1)
    print('Servidor TCP: {}:{}'.format(host,port))
    
    while True:

        # fica bloqueado aguardando a conexão de um cliente
        conn, addr = socketTCP.accept()
        
        lista.append(conn)
        
        print ("Conexão realizada por: " + str(addr))
        # cria e dispara a execução da thred do cliente
        t = threading.Thread(target=rodaThread, args=(conn,))
        t.start()
        
    socket.close()
    
if __name__ == '__main__':
    Main()