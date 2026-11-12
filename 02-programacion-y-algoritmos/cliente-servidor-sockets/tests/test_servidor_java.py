import socket
import struct
import pytest

@pytest.fixture
def conexion_servidor():
    # Asegúrate de que MiServidor.java esté corriendo en el puerto 8080 antes de ejecutar el test
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8080))
    yield s
    s.close()

def test_servidor_java_frase_y_suma(conexion_servidor):
    s = conexion_servidor
    
    # 1. Empaquetar el comando "/frase" según el formato writeUTF de Java:
    # 2 bytes para la longitud de la cadena + los bytes de la cadena en UTF-8
    comando = "/frase"
    encoded_comando = comando.encode('utf-8')
    paquete_comando = struct.pack(f'>H{len(encoded_comando)}s', len(encoded_comando), encoded_comando)
    
    # 2. Empaquetar n1 (5) y n2 (10) como enteros de 4 bytes (big-endian '>ii')
    n1 = 5
    n2 = 10
    paquete_numeros = struct.pack('>ii', n1, n2)
    
    # Enviar la petición completa al servidor Java
    s.sendall(paquete_comando + paquete_numeros)
    
    # --- LEER LA RESPUESTA DEL SERVIDOR ---
    
    # Leer los primeros 2 bytes para saber la longitud de la frase devuelta
    longitud_bytes = s.recv(2)
    assert len(longitud_bytes) == 2, "No se pudo leer la longitud de la respuesta"
    (longitud_frase,) = struct.unpack('>H', longitud_bytes)
    
    # Leer la frase exacta utilizando los bytes medidos
    frase_bytes = s.recv(longitud_frase)
    frase = frase_bytes.decode('utf-8')
    
    # Leer los 4 bytes correspondientes a la suma enviada con output.writeInt(suma)
    suma_bytes = s.recv(4)
    assert len(suma_bytes) == 4, "No se pudo leer el valor de la suma"
    (suma,) = struct.unpack('>i', suma_bytes)
    
    # 3. Validar los resultados
    assert suma == 15, f"Se esperaba 15 como suma y se obtuvo {suma}"
    
    frases_esperadas = ["Hola", "Adios", "Buenos Dias", "Buenas Noches", "Hasta Luego"]
    assert frase in frases_esperadas, f"La frase '{frase}' no está en la lista del servidor"