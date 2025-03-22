import threading
import time

Contador = 0 # Recurso compartilhado

L = threading.Lock() # bloqueia o uso da variavel já declaradas em diferente threads simultaneos 

def Incrementar():
    global Contador 
    for _ in range(1000):
        L.acquire() # Ativa o bloqueio 

        try: 
            x = Contador
            time.sleep(0.00001)
            x = x + 1
            Contador = x
        finally:
            L.release() # Desbloqueia aqui

TA = threading.Thread(target = Incrementar)
TB = threading.Thread(target = Incrementar)
TC = threading.Thread(target = Incrementar)

TA.start()
TB.start()
TC.start()

TA.join()
TB.join()
TC.join()

print(f'Contador: {Contador}')
