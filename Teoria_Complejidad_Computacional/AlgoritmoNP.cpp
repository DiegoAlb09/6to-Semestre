#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <ctime>

unsigned t0, t1;

using namespace std;
int main(){
  t0 = clock();
  int n = 100, menor = 1;
  int U[n];

  cout << "El arreglo U es: " << endl;
  for (int i = 0; i < n; i++){
    U[i] = rand() % 100 + 1;
    cout << U[i] << " ";
  }

  int num = pow(2, n-1);
  int div = num;
  int g[n];

  int sumaA = 0, sumaB = 0, suma = 0, menorSuma = 10000;
  int combinacion[n];

  while(num != 0){
    int numG = num, divG = div;

    cout << "\n\t Numeros binarios" << endl;
    cout << "Numero: " << num << " en binario: ";
    for (int i = 0; divG != 0; i++){
      if(numG/divG == 1){
        g[i] = 1;
        numG -= divG;
      }else{
        g[i] = 0;
      }
      divG /= 2;
      cout << g[i] << " ";
    }

    sumaA = 0, sumaB = 0, suma = 0;

    for(int j = 0; j < n; j++){
      if(g[j] == 1){
        sumaA += U[j];
      }else{
        sumaB += U[j];
      }
    }
    cout << "\n\t Suma A: " << sumaA << " Suma B: " << sumaB << endl;

    suma = abs(sumaA - sumaB);
    cout << "Valor absoluto: " << suma << endl;

    if(suma < menorSuma){
      for(int k = 0; k < n; k++){
        combinacion[k] = g[k];
      }
      cout << "Mejor combinacion.";
      menorSuma = suma;
    }else{
      cout << "La nueva combinacion es peor.";
    }
    cout << endl;
    num--;      
  }
  cout << endl << "La mejor combinacion es: ";
  for(int i = 0; i < n; i++){
    cout << combinacion[i] << " ";
  }
  cout << endl << "Conjunto A: ";
  for(int i = 0; i < n; i++){
    if(combinacion[i] == 1){
      cout << U[i] << " ";
    }
  }
  cout << endl << "Conjunto B: ";
  for(int i = 0; i < n; i++){
    if(combinacion[i] == 0){
      cout << U[i] << " ";
    }
  }

  cout << endl;

  t1 = clock();
  double time = (double(t1-t0)/CLOCKS_PER_SEC);
  cout << "Tiempo de ejecucion: " << time << endl;
}
