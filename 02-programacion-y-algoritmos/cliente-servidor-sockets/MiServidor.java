 import java.net.*;
import java.io.DataInputStream;
import java.util.ArrayList;
import java.io.DataOutputStream;

public class MiServidor {
    public static void main(String[] args) {
        ArrayList<String> ListaDeFrases = new ArrayList<>();
        ListaDeFrases.add("Hola");
        ListaDeFrases.add("Adios");
        ListaDeFrases.add("Buenos Dias");
        ListaDeFrases.add("Buenas Noches");
        ListaDeFrases.add("Hasta Luego");

        try (ServerSocket serverSocket = new ServerSocket(8080)) {
            System.out.println("Servidor Inciado. Escuchando en el puerto 8080...");

            try (Socket socket = serverSocket.accept();
                 DataInputStream input = new DataInputStream(socket.getInputStream());
                 DataOutputStream output = new DataOutputStream(socket.getOutputStream())) {

                System.out.println("Cliente Conectado!");

                String message = input.readUTF();
                int n1 = input.readInt();
                int n2 = input.readInt();
                int suma = n1 + n2;

                if (message.equals("/frase")) {
                    int indiceAleatorio = (int) (Math.random() * ListaDeFrases.size());
                    String fraseElegida = ListaDeFrases.get(indiceAleatorio);
                    output.writeUTF(fraseElegida);
                } else {
                    output.writeUTF("Error 404: Ruta no encontrada");
                }

                output.writeInt(suma);
                output.flush();

            }
        } catch (Exception e) {
            System.out.println("Server Error: " + e);
        }
    }
}