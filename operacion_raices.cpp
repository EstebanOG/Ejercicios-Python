//#include "raiz.h"
#include<iostream>
#include<cmath>
/*#pragma once*/

using namespace std;

void leerCoeficientes (float &a, float &b, float &c){
	cout << "Ingrese los valores de a b y c de la ecuacion" << endl;
	cin >> a >> b >> c;
}

int discriminante (float a, float b, float c, float &disc, int &tiporaiz){
	if (a != 0)
	{
		disc = (b*b) - (4 * (a)*(c));
		if (disc == 0)
			tiporaiz = 0;
		else if(disc > 0)
			tiporaiz = 1;
		else 
			tiporaiz = -1;
	}

return tiporaiz;
}
void raicesIguales(float a, float b, float &x1,float &x2,float disc){
	x1 = x2 = (-b*disc / (2 * a));
	
	cout << "los tipos de raices son iguales" << endl;
	cout << "El valor de la raiz es de = " << discriminante << endl;
	cout << "Los resultados de la ecuacion es" << endl;
	cout << "x1=" << x1 << endl;
	cout << "x2=" << x2 << endl;
}

void raicesNormales(float a, float b, float &x1, float &x2, float &disc  ){
	x1 = (((-1 * (b)) - sqrt(disc)) / 2 * a);
	x2 = (((-1 * (b)) + sqrt(disc)) / 2 * a);
	cout << "los tipos de raices son normales" << endl;
	cout << "El valor de la raiz es de = " << disc << endl;
	cout << "Los resultados de la ecuacion es" << endl;
	cout << "x1=  " << x1 << endl;
	cout << "x2 = " << x2 << endl;
}

void raicesImaginarias(float a, float b, float &x1, float &x2, float &disc ){
	x1 = (-b +(disc))/ (2 * a);
	x2 = (-b+-(disc))/ ( 2*a);

	cout << "los tipos de raices son imaginarias" << endl;
	cout << "El valor de la raiz es de = " << disc<< endl;
	cout << "Los resultados de la ecuacion es" << endl;
	cout << "x1=" << x1 << " + " << x2 << "i" << endl;
	cout << "x2=" << x1 << " - " << x2 << "i" << endl;
}

int main(void){
	float a, b, c;
	float x1, x2, disc;
	int tiporaiz;
	leerCoeficientes(a, b, c);
	tiporaiz = discriminante(a, b, c, disc,tiporaiz);

	switch (tiporaiz){
		case 0:
			raicesIguales(a, b, x1, x2,disc);
		break;
		case 1:
			raicesNormales(a, b,  x1, x2, disc);
		break;
		case -1:
			raicesImaginarias(a, b, x1, x2, disc);
		default:
		cout << "opcion invalida" << endl;
	}
	
	system("pause");
}

