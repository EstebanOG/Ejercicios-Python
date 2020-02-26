#include<iostream>
#include<cmath>

using namespace std;

void leerCoeficientes (float &a, float &b, float &c){
	cout << "Ingrese los valores de los coeficientes(a, b y c) de la ecuacion" << endl;
	cout<<"a: ";
	cin >> a;
	cout<<"b: ";
	cin >> b;
	cout<<"c: ";
	cin >> c;
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
	x1 = x2 = (-b / (2 * a));
	
	cout<<"El discriminante es cero, por lo cual tiene una unica solucion."<<endl;
	cout << "El resultado de la ecuacion es: " << endl;
	cout << "x1 = " << x1 << endl;
	cout << "x2 = " << x2 << endl;
}

void raicesNormales(float a, float b, float &x1, float &x2, float &disc  ){
	x1 = (((-1 * (b)) - sqrt(disc)) / 2 * a);
	x2 = (((-1 * (b)) + sqrt(disc)) / 2 * a);
	cout<<"El discriminante es mayor a cero, por lo cual tiene dos soluciones reales."<<endl;
	cout << "El resultado de la ecuacion es: " << endl;
	cout << "x1 = " << x1 << endl;
	cout << "x2 = " << x2 << endl;
}

void raicesImaginarias(float a, float b, float &x1, float &x2, float &disc ){
	
	x1 = (-b +(disc))/ (2 * a);
	x2 = (-b+-(disc))/ ( 2*a);

	cout<<"El discriminante es menor a cero, por lo cual tiene una dos soluciones."<<endl;
	cout << "El resultado de la ecuacion es: " << endl;
	cout << "x1=" << x1 << " + " << x2 << "i" << endl;
	cout << "x2=" << x1 << " - " << x2 << "i" << endl;
}

int main(void){
	float a, b, c;
	float x1, x2, disc;
	int tiporaiz;
	cout<<"Programa para calcular la solucion de la ecuacion expresada de la siguiente manera ax^2+bx+c=0"<<endl;
	cout<<"----------------------------------------------------------------------------------------------"<<endl<<endl;
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
		break;
		default:
		cout << "Opcion invalida" << endl;
	}
	
	system("pause");
}

