pessoa pessoa = new pessoa();
pessoa pessoa2 = new pessoa();

pessoa.nome = "lucas";
pessoa2.nome = "esfolha";


List<pessoa> pessoas = new List<pessoa>();
pessoas.Add(pessoa);
pessoas.Add(pessoa2);
       

foreach (var item in pessoas)
{
    Console.WriteLine(item.nome);          
}