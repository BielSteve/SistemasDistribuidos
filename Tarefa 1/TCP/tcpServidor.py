import socket
import threading

def rodaThread(conn):
    while True:

        print('Esperando mensagens...')
        data = conn.recv(1024)
        if not data:
            break
        
        print('Recebido {} bytes de {}'.format(len(data), conn.getpeername()))


        # devolve a mensagem para o cliente
        conn.send(data.upper())


    conn.close()
    return


def Main():

    host = "0.0.0.0"
    port = 10000
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.bind((host,port))
    socketTCP.listen(1)
    print('Servidor TCP: {}:{}'.format(host,port))
    
    while True:
        
        # fica bloqueado aguardando a conexão de um cliente
        conn, addr = socketTCP.accept()
        print ("Conexão realizada por: " + str(addr))
        # cria e dispara a execução da thred do cliente
        t = threading.Thread(target=rodaThread, args=(conn,))
        t.start()
        
    socket.close()
    
if __name__ == '__main__':
    Main()