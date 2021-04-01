import socket
#cria o socket e conecta ao servidor
sock = socket.socket()
sock.connect(('localhost', 12345))
#tamanho do buffer
CHUNK_SIZE = 8 * 1024
#cria um novo arquivo, vazio, para receber o arquivo enviado
arq = open('zedosteste.jpg', 'wb')
#recebe os primeiros bytes do arquivo
chunk = sock.recv(CHUNK_SIZE)
#fica em loop recebendo as outras partes do arquivo
while chunk:
    #escreve os bytes recebidos no arquivo
    arq.write(chunk)
    #aguarda o envio de novos bytes
    chunk = sock.recv(CHUNK_SIZE)
    
#fecha o arquivo
arq.close()
#fecha o socket
sock.close()