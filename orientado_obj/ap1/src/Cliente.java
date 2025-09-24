public class Cliente {
    private String nome;
    private int anoNacsimento;
    private Endereco endereco;

    public Cliente(String nome, int anoNacsimento, Endereco endereco){
        this.nome = nome;
        this.anoNacsimento = anoNacsimento;
        this.endereco = endereco;
    }

    public String getNome() {
        return nome;
    }

    public int getAnoNacsimento() {
        return anoNacsimento;
    }

    public Endereco getEndereco() {
        return endereco;
    }
}
