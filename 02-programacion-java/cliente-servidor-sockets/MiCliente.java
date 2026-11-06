import java.net.*;
import java.io.DataOutputStream;
import java.io.DataInputStream;
import java.util.Scanner;

public class MiCliente {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un numero para enviar al servidor: ");
        String n1 = scanner.nextLine();
        System.out.println("Ingrese otro numero para enviar al servidor: ");
        String n2 = scanner.nextLine();

        try (Socket s = new Socket("localhost", 8080);
             DataOutputStream d = new DataOutputStream(s.getOutputStream());
             DataInputStream input = new DataInputStream(s.getInputStream())) {

                d.writeUTF("/frase");
                d.writeInt(Integer.parseInt(n1));
                d.writeInt(Integer.parseInt(n2));
            d.flush();
            String respuesta = input.readUTF();
            int suma = input.readInt();
            System.out.println("Respuesta del servidor: " + respuesta + ", Suma: " + suma);

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}