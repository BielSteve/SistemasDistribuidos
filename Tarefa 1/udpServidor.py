import socket

def Main():
    host = "127.0.0.1"
    port = 10000
    # cria o socket UDP do servidor (Internet,Transporte)
    socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Configura o IP e a porta que o servidor vai ficar executando
    socketUDP.bind((host,port))
    a = "- Abc Bolinhas"
    print('Servidor UDP: {}:{}'.format(host,port))
    while True:
        print('Esperando mensagens...')
        data, address = socketUDP.recvfrom(4096) # buffer size - bytes
        print('Recebido {} bytes de {}'.format(len(data), address))
        print(data)
        
        if data:
            sent = socketUDP.sendto(data.upper()+str(a), address)
        else:
            break

    socketUDP.close()

if __name__ == '__main__':
    Main()