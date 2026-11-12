import socket
import struct
import subprocess
import threading
import pytest

@pytest.fixture
def mock_servidor_tcp():
    """Levanta un servidor TCP temporal en Python para simular a MiServidor"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(1)
    server_socket.settimeout(4.0)
    
    datos_recibidos = {}

    def escuchar():
        try:
            conn, _ = server_socket.accept()
            with conn:
                # 1. Leer el comando /frase enviado por MiCliente (DataOutputStream.writeUTF)
                long_cmd_bytes = conn.recv(2)
                (long_cmd,) = struct.unpack('>H', long_cmd_bytes)
                datos_recibidos["comando"] = conn.recv(long_cmd).decode('utf-8')
                
                # 2. Leer n1 y n2 enviados por MiCliente (DataOutputStream.writeInt -> 4 bytes c/u)
                (datos_recibidos["n1"],) = struct.unpack('>i', conn.recv(4))
                (datos_recibidos["n2"],) = struct.unpack('>i', conn.recv(4))
                
                # 3. Responder al cliente simulando la lógica del servidor Java
                frase_respuesta = "Hola"
                suma_total = datos_recibidos["n1"] + datos_recibidos["n2"]
                
                # Empaquetar respuesta en formato Java (writeUTF + writeInt)
                encoded_frase = frase_respuesta.encode('utf-8')
                paquete_respuesta = (
                    struct.pack(f'>H{len(encoded_frase)}s', len(encoded_frase), encoded_frase) +
                    struct.pack('>i', suma_total)
                )
                conn.sendall(paquete_respuesta)
        except socket.timeout:
            pass
        finally:
            server_socket.close()

    # Iniciar el servidor mock en un hilo para que no bloquee el test
    hilo_servidor = threading.Thread(target=escuchar)
    hilo_servidor.start()
    
    yield datos_recibidos
    
    hilo_servidor.join()

def test_mi_cliente_interaccion(mock_servidor_tcp):
    # Compilar el cliente Java por si hubo cambios (opcional si ya está compilado)
    subprocess.run(["javac", "MiCliente.java"], check=True)
    
    # Ejecutar MiCliente pasando "7" y "8" como si el usuario los escribiera en la consola
    resultado = subprocess.run(
        ["java", "MiCliente"],
        input="7\n8\n",
        text=True,
        capture_output=True,
        timeout=5
    )
    
    # Validar que el programa Java finalizó correctamente sin excepciones
    assert resultado.returncode == 0, f"Error en la ejecución de Java: {resultado.stderr}"
    
    # Validar que el servidor mock recibió exactamente los datos enviados por el cliente
    assert mock_servidor_tcp["comando"] == "/frase"
    assert mock_servidor_tcp["n1"] == 7
    assert mock_servidor_tcp["n2"] == 8
    
    # Validar que el cliente leyó e imprimi la respuesta correcta en su consola
    assert "Respuesta del servidor: Hola, Suma: 15" in resultado.stdout