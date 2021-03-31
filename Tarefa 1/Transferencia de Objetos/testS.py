import socket

#arquivo para enviar
file_path = "ServidorArquivo.py"

#cria o socket
server_socket = socket.socket()
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
#aguarda novos clientes

#ao receber a conexao de um novo cliente, envia o arquivo escolhido para ele
while True:
    client_socket, addr = server_socket.accept()
    #abre o arquivo escolhido, e vai enviando para o cliente por partes
    with open( file_path , 'rb') as f:
        client_socket.sendfile(f, 0)
    #fecha o socket do cliente
    client_socket.close()