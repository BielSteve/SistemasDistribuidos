//ServidorRMI.java
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;


public class ServidorRMI implements InterfaceRemotaRMI {
    // Implementacao do metodo da interface que pode ser invocado remotamente
    public boolean isPar(int n)
    {
        System.out.println("Requisição recebida com o seguinte argumento: " + n);
        return n % 2 == 0;
    }


    public static void main(String args[]) 
    {
        try {
            ServidorRMI obj = new ServidorRMI();
            // Importante: nao tirar o "0" do segundo argumento do metodo exportObject
            // Se nao a JVM nao gera o stub automaticamente e buscara um ServidorRMI_stub.class em tempo de execucao.
            // Nesse caso teria que ser utilizado o rmic para gerar a ServidorRMI_stub.class
            // Maiores detalhes em http://java.sun.com/j2se/1.5.0/docs/guide/rmi/relnotes.html
            // Exporta o objeto remoto colocando-o em listening para receber request numa porta anonima TCP - retorna o stub do objeto servidor
            InterfaceRemotaRMI stub = (InterfaceRemotaRMI) UnicastRemoteObject.exportObject(obj, 0);
            String refRemota = stub.toString();
            System.out.println("Stub Gerado: " + refRemota.substring(refRemota.indexOf("endpoint")));
            // Tenta localizar o rmiregistry no host local na porta default (1099), caso nao encontre, retorna erro: RemoteException
            //Registry registro = LocateRegistry.getRegistry();
            ////Runtime.getRuntime().exec("rmiregistry 1099");
            Registry registro = LocateRegistry.createRegistry(1099);
            refRemota = registro.toString();
            System.out.println("Registro: " + refRemota.substring(refRemota.indexOf("endpoint")));
            // Registra o objeto servidor atraves de um nome "AbcBolinhas" e de sua interface "stub"
            // Se o string AbcBolinhas ja estiver associado a outro objeto remoto, ocorre uma excecao
            registro.rebind("AbcBolinhas", stub);
            System.out.println("Servidor pronto!!!");
        } 
        catch (Exception e) {
            System.out.println("Erro no servidor:"+e.getMessage());
        }
    }
}