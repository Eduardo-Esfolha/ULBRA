package ex4;

public class Bateria {
    private int capacidade;
    private int pctAtual;

    public Bateria(int capacidade, int pctAtual){
        this.capacidade = capacidade;
        this.pctAtual = pctAtual;
    }

    public int getCapacidade() {
        return capacidade;
    }

    public int getPctAtual() {
        return pctAtual;
    }
}
