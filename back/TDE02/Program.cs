using System.ComponentModel;

Console.WriteLine("digite um numero:");
Double num1 = Convert.ToDouble(Console.ReadLine());

Console.WriteLine("digite o segundo numero:");
double num2 = Convert.ToDouble(Console.ReadLine());

double soma = num1 + num2;
double sub = num1 - num2;
double mul = num1 * num2;
double div = num1 / num2;


Console.WriteLine("a soma de " + num1 + "E" + num2 + "é igual a " + soma);
Console.WriteLine($"a subtração de{num1} e {num2} é igual a {sub}");
Console.WriteLine("a multiplicação de {0} com {1} é igual a {2} ", num1, num2, mul);