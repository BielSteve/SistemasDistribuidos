//ClienteRMI.java
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
 
public class ClienteRMI 
{
    public static void main(String[] args) 
    {
        try 
        {
            // localiza o registro
            // obtém o stub para o registro
            Registry registry = LocateRegistry.getRegistry("127.0.0.1" , 1099);

            // localiza o serviço registrado como AbcBolinhas
            InterfaceRemotaRMI stub = (InterfaceRemotaRMI) registry.lookup("AbcBolinhas");

            // realiza a invocacao remota do metodo isPar(n)
            System.out.println("3 é par: " + stub.isPar(3));
            System.out.println("100 é par: " + stub.isPar(100));
        } 
        catch (Exception e) {
            System.err.println("! Erro no cliente: " + e.toString());
        }
    }
}