#include <stdio.h>

int main()
{

    float a;
    float b;
    float risultato;

    printf("Inserisci il primo numero: ");
    scanf("%f", &a);

    printf("Inserisci il secondo numero: ");
    scanf("%f", &b);

    risultato = ((a + b) / 2);

    printf("Il risultato è: %g", risultato);

    return 0;
}