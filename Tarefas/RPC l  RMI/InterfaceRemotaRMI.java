//InterfaceRemotaRMI.java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceRemotaRMI extends Remote {
    boolean isPar(int n) throws RemoteException;
}