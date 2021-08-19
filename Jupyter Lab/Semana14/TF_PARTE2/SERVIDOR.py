# -*- coding: utf-8 -*-
import socket
import threading
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
HEADER_SIZE = 10

class Server:
    def __init__(self):
        # Lista con los sockets de los clientes
        self.connections = []
        # Se establece el socket del servidor
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Permitir eliminar el error "socket already in use"
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((HOST, PORT))
        self.sock.listen()
        
    def run(self):
        print("Servidor iniciado. Esperando conexiones...")
        while True:
            # Se aceptan las conexiones entrantes
            conn, addr = self.sock.accept()    # blocking
            
            # Generar un thread para atender la conexion del cliente
            th = threading.Thread(target=self.handler, args=(conn, addr), daemon=True)
            th.start()
            
            # Informar de la conexion entrante
            print(str(addr[0]) + ":" + str(addr[1]), "conectado")
            
            # Se agrega el socket del cliente en la lista de conexiones
            self.connections.append(conn)
        
    def handler(self, conn, addr):
        while True:
            # Si es que no hay problemas con la conexion...
            try:
                # Lee el encabezado y los datos entrantes
                data_header = conn.recv(HEADER_SIZE)
                data = conn.recv(int(data_header))
                
                # Se hace un broadcast a los otros sockets
                for connection in self.connections:
                    connection.send(data_header + data)
                                
            # ... el cliente se ha desconectado
            except:
                print(str(addr[0]) + ":" + str(addr[1]), "desconectado")
                self.connections.remove(conn)
                conn.close()
                break
            
def main():
    server = Server()
    server.run()
        
if __name__ == "__main__":
    main()