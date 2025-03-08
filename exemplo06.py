import threading
import time

Contador = 0  # Recurso compartilhado

L = threading.Lock()  # Bloqueio para proteger o acesso ao recurso compartilhado

def Incrementar():
    global Contador
    for _ in range(5000):
        x = Contador
        time.sleep(0.0001)  # Simula um pequeno atraso
        x = x + 1
        Contador = x

# Lista para armazenar as threads
ListaDeThreads = []

# Cria e inicia as threads
for _ in range(50):
    t = threading.Thread(target=Incrementar)
    ListaDeThreads.append(t)
    t.start()

# Espera todas as threads terminarem
for t in ListaDeThreads:
    t.join()

print(f'Valor final do contador: {Contador}')
