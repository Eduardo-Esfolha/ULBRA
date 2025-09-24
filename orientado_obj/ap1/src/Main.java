
public class Main {

    public static void main(String[] args) {
        Estado estado = new Estado("rio grande do sul");
        Municipio municipio = new Municipio("imbé", estado);
        Endereco endereco = new Endereco("casa", 898, "santa terezinha", 95625000, municipio);
        Cliente cliente = new Cliente("esfolha", 2004, endereco);
        System.out.println("o nome do cliente é: " + cliente.getNome()+ " o logradouro é: " + cliente.getEndereco().getLogradouro() + " o municipio é: " + cliente.getEndereco().getMunicipio().getNome() + " e o estado é: " +cliente.getEndereco().getMunicipio().getEstado().getNome());
    }
}