/*int x = 10;

double y = x;
double pi = 3.14;

int num = (int)pi;

string numerotexto = "123";
int numero = Convert.ToInt32(numerotexto);

string nome = "lucas";
int idade = 33;


//concatena
string mensagem = "ola meu nome e " + nome + " e eu tenho " + idade + " anos.";

//interpolaçao
string mensagemInterpolada = $"ola meu nome e {nome} e eu tenho {idade} anos.";

// spaceholder
string mensagemplaceholder = string.Format("ola meu nome e {0} e eu tenho {1} anos.", nome, idade);

Console.WriteLine(mensagem);
Console.WriteLine(mensagemInterpolada);
Console.WriteLine(mensagemplaceholder);
*/
Console.WriteLine("digite seu nome:");
string nome = Console.ReadLine();

Console.WriteLine("digite sua idade:");
int idade = Convert.ToInt32(Console.ReadLine());

Console.WriteLine($"meu nome é {nome} e minha idade é {idade}");