#include <stdio.h>

int main()
{
    int a;
    int b;
    int risultato;

    printf("Inserisci il primo numero: ");
    scanf("%d", &a);
    // %d rappresenta un numero intero

    printf("Inserisci il secondo numero: ");
    scanf("%d", &b);

    risultato = a * b ;

    printf("Il risultato è; %d", risultato );

    return 0;
}