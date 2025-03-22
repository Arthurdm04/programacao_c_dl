# Servidor

import socket
from datetime import datetime

def iniciar_Servidor():

    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.bind((HOST, PORT))
        S.listen()
        print(f'Servidor executando em {HOST}:{PORT}')
        while True:
            conn, addr = S.accept()
            with conn:
                print(f'Conexão com {addr}')
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data.decode() == 'data e hora':
                        agora = datetime.now().strftime('%y - %m - %d %H:%M:%S')
                        resposta = f'Data e hora: {agora}'
                        conn.sendall(resposta.encode())
                    elif data.decode().strip().lower() == 'bom dia':
                        resposta = f'Olá, {addr}. Bom dia para você também!'
                        conn.sendall(resposta.encode())
                    else:
                        resposta = 'Mensagem inválida!'
                        conn.sendall(resposta.encode())
if __name__ == '__main__':
    iniciar_Servidor()
