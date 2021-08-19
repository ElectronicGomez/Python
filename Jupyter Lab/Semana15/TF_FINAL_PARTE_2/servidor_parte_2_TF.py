# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:28:23 2020

@author: ASUS
"""

#%%
import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PUERTO = 2000
HEADER_SIZE = 10

class Servidor:
    def __init__(self):
        self.Conexiones_disp = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((HOST, PUERTO))
        self.sock.listen()
        
    def run(self):
        print("Se ha iniciado el servidor. Esperando conexiones...")
        while True:
            conn, addr = self.sock.accept()
            th = threading.Thread(target=self.handle, args=(conn, addr), daemon=True)
            th.start()
            print(str(addr[0]) + ":" + str(addr[1]), "Conectado")
            self.Conexiones_disp.append(conn)
        
    def handle(self, conn, addr):
        while True:
            try:
                data_header = conn.recv(HEADER_SIZE)
                data = conn.recv(int(data_header))
                for connection in self.Conexiones_disp:
                    connection.send(data_header + data)
            except:
                print(str(addr[0]) + ":" + str(addr[1]), "Desconectado")
                self.Conexiones_disp.remove(conn)
                conn.close()
                break
            
def main():
    serv = Servidor()
    serv.run()
        
if __name__ == "__main__":
    main()