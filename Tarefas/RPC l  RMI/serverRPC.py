# ServidorRPC.py
from xmlrpc.server import SimpleXMLRPCServer


def is_par(n):
    
    print("Requisição recebida com o seguinte argumento: " + str(n))
    return n % 2 == 0

def is_impar(n):
    
    print("Requisição recebida com o seguinte argumento: " + str(n))
    return n % 2 != 0

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_par, "is_NumeroPar")
server.register_function(is_par, "is_NumeroImpar")

server.serve_forever()