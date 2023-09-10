import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Laberinto {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Leer archivo de texto
        char[][] laberinto = leerLaberintoDesdeArchivo("laberinto.txt");

        if (laberinto != null) {
            // Leer filas y columnas
            int filas = laberinto.length;
            int columnas = laberinto[0].length;
            // Preguntar posicion de inicio
            System.out.print("En qué posición deseas iniciar (1-" + columnas + "): ");
            int columnaInicio = scanner.nextInt() - 1; // Restamos 1 porque los índices comienzan en 0
            // Verificar posicion valida
            if (columnaInicio >= 0 && columnaInicio < columnas) {
                // Encontrar la ruta
                List<String> ruta = encontrarRuta(laberinto, 0, columnaInicio); // Fila de inicio siempre es 0
                // Mostrar ruta
                System.out.println("Ruta:");
                for (String paso : ruta) {
                    System.out.println(paso);
                }
            } else {
                System.out.println("Columna de inicio no válida.");
            }
        } else {
            System.out.println("No se pudo leer el laberinto desde el archivo.");
        }
    }

    public static char[][] leerLaberintoDesdeArchivo(String nombreArchivo) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(nombreArchivo));
            String primeraLinea = br.readLine();
            String[] dimensiones = primeraLinea.split(" ");
            int filas = Integer.parseInt(dimensiones[0]);
            int columnas = Integer.parseInt(dimensiones[1]);
            char[][] laberinto = new char[filas][columnas];
            for (int i = 0; i < filas; i++) {
                String linea = br.readLine();
                laberinto[i] = linea.toCharArray();
            }
            br.close();
            return laberinto;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static List<String> encontrarRuta(char[][] laberinto, int fila, int columna) {
        List<String> ruta = new ArrayList<>();
        encontrarRutaRecursivo(laberinto, fila, columna, ruta);
        return ruta;
    }

    private static boolean encontrarRutaRecursivo(char[][] laberinto, int fila, int columna, List<String> ruta) {
        int filas = laberinto.length;
        int columnas = laberinto[0].length;
        // Verificar si es el final del laberinto
        if (fila == filas - 1) {
            ruta.add("[FILA: " + (fila + 1) + " COLUMNA: " + (columna + 1) + "]");
            return true;
        }
        // Verificar que la posicion actual sea 0
        if (fila >= 0 && fila < filas && columna >= 0 && columna < columnas && laberinto[fila][columna] == '0') {
            // Marcar la posición actual como visitada
            laberinto[fila][columna] = 'X'; // Para evitar ciclos
            // Agregar la posicion actual a la ruta
            ruta.add("[FILA: " + (fila + 1) + " COLUMNA: " + (columna + 1) + "]");
            // Explorar hacia abajo
            if (encontrarRutaRecursivo(laberinto, fila + 1, columna, ruta)) {
                return true;
            }
            // Explorar hacia la izquierda
            if (encontrarRutaRecursivo(laberinto, fila, columna - 1, ruta)) {
                return true;
            }
            // Explorar hacia la derecha
            if (encontrarRutaRecursivo(laberinto, fila, columna + 1, ruta)) {
                return true;
            }
            // Retroceder si no se encontro una ruta valida desde esta posicion
            ruta.remove(ruta.size() - 1);
        }
        return false;
    }
}
