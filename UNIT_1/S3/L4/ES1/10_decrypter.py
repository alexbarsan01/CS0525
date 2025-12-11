from typing import Callable

# Funzione per shiftare i caratteri maiuscoli e minuscoli
def shift_char(c: str, k: int) -> str:
    if 'A' <= c <= 'Z':
        return chr((ord(c) - ord('A') + k) % 26 + ord('A'))
    if 'a' <= c <= 'z':
        return chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    return c

# Applica lo shift k al testo (positivo o negativo)
def caesar(text: str, k: int) -> str:
    return ''.join(shift_char(c, k) for c in text)

# Cifra il testo con shift positivo
def encrypt(plaintext: str, k: int) -> str:
    return caesar(plaintext, k)

# Decifra il testo con shift negativo
def decrypt(ciphertext: str, k: int) -> str:
    return caesar(ciphertext, -k)

# Prova tutte le chiavi
def bruteforce(ciphertext: str) -> dict:
    return {k: decrypt(ciphertext, k) for k in range(26)}

def main():
    print("Cifrario di Cesare")

    mode = input("Scegli 'e' per cifrare, 'd' per decifrare, 'b' per brute-force: ").strip().lower()

    if mode not in ('e', 'd', 'b'):
        print("Modalità non valida.\nFine programma.")
        return

    # modalità brute-force
    if mode == 'b':
        ct = input("Inserisci il testo cifrato: ")

        while True:
            scelta = input("Inserisci una k (0-25) oppure 'exit' per uscire: ").strip().lower()

            # uscita
            if scelta in ("exit", "e", "q"):
                print("Uscita dalla modalità brute-force.")
                return

            # validazione input numerico
            if not scelta.isdigit():
                print("Devi inserire un numero da 0 a 25, oppure 'exit'.")
                continue

            k = int(scelta)
            if not 0 <= k <= 25:
                print("La k deve essere tra 0 e 25.")
                continue

            # mostra la decifratura con quella k
            print(f"k={k:2d}: {decrypt(ct, k)}")

        return

    # cifratura/decifratura normale
    text = input("Inserisci il testo: ")

    try:
        k = int(input("Inserisci lo shift (numero intero): ").strip())
    except ValueError:
        print("Shift non valido. Devi inserire un numero intero.")
        return

    if mode == 'e':
        print("Testo cifrato:", encrypt(text, k))
    else:
        print("Testo decifrato:", decrypt(text, k))


if __name__ == "__main__":
    main()
