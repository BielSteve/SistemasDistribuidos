import socket
import threading
import json



class Mensagem(object):
    def __init__(self):
        self.usuario = ''
        self.msg = ''

#cria um vetor
lista = []

def rodaThread(conn):
    while True:
        
        print('Esperando mensagens...')
        #recebe mensagem do usuário
        data = conn.recv(4096)
        
        
        if object:
            #desserializa a mensagem recebida, disponibilizando o objeto novamente na memoria
            objetoRecebido = json.loads(data)
            print( objetoRecebido )
            #mostra os dados do objeto
            print( objetoRecebido.get("usuario") )
            print( objetoRecebido.get("msg") )
            
            
            
            
        else:
            
            if (data.decode() == 'q'):
                break
            
            if (data):

                #transformando o data em string e colocando na nova variavel nova
                nova = data.decode()
                
                #aqui eu uso a função find para procurar o opetador +
                if nova.find('+') > 0:
                    #aqui eu faço a separação
                    valor = nova.split('+')
                    mensagem_f = valor[0] + ' >>> ' + valor[1]
                
                    #percorrendo o vetor lista
                    for x in lista:
                        
                        #se a conexão for diferente de conexão na posição x
                        if conn != x:
                            try:
                                #enviar mensagem para o outro usuario
                                x.send(mensagem_f.encode())
                            except:
                                print('tomara que de certo')
            #remover conexões   
            else:
                removerConexao(conn)
                break
            
        



    conn.close()
    return

def removerConexao(conn):
    if conn in lista:
        conn.close()
        lista.remove(conn)
        

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
        
        #adiciona item ao final da lista
        lista.append(conn)
        
        print ("Conexão realizada por: " + str(addr))
        # cria e dispara a execução da thred do cliente
        t = threading.Thread(target=rodaThread, args=(conn,))
        t.start()
        
    socket.close()
    
if __name__ == '__main__':
    Main()