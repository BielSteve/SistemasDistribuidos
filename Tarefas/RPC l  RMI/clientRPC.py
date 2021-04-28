# ClienteRPC.py
import xmlrpc.client


with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("3 é par: %s" % str(proxy.is_NumeroPar(3)))
    print("100 é par: %s" % str(proxy.is_NumeroPar(100)))
    print("99 é par: %s" % str(proxy.is_NumeroImpar(99)))
    