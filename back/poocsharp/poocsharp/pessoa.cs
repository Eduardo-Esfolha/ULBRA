public class pessoa
{
    public int idade;

    public string nome;


    public pessoa(string novonome)
    {
        nome = novonome;
    }

    public pessoa()
    {
        nome = "conta";
    }

    public void falar()
    {
        Console.WriteLine($"meu nome é: {nome} e tenho {idade} anos.");

    }

    public int getIdade()
    {
        return idade;
    }

    public void setidade(int novaidade)
    {
        if (idade <= 0)
        {
            idade = novaidade;
        }
        else
        {
            Console.WriteLine("erro");
        }
        
    }
}