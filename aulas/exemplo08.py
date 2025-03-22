import socket # pip install socket / se necessário

hostname = socket.gethostname()
ip_local = socket.gethostbyaddr(hostname)

print(f'Nome do host: {hostname}')
print(f'Endereço do host: {ip_local}')
