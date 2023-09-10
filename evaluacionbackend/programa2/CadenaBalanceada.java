import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Stack;

public class CadenaBalanceada {
    public static void main(String[] args) {
        String nombreArchivo = "parentesis.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {
            String linea;
            int numeroLinea = 1;

            while ((linea = br.readLine()) != null) {
                if (verificarBalance(linea)) {
                    System.out.println("Línea " + numeroLinea + ": Correctamente balanceada");
                } else {
                    System.out.println("Línea " + numeroLinea + ": Incorrectamente balanceada");
                }
                numeroLinea++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static boolean verificarBalance(String cadena) {
        Stack<Character> pila = new Stack<>();
        for (char caracter : cadena.toCharArray()) {
            if (caracter == '(') {
                pila.push(caracter);
            } else if (caracter == ')') {
                if (pila.isEmpty()) {
                    return false; //Hay un cierre sin apertura correspondiente
                }
                pila.pop(); //Se encontro una apertura correspondiente
            }
        }
        return pila.isEmpty(); //Si la pila esta empty esta balanceada
    }
}
