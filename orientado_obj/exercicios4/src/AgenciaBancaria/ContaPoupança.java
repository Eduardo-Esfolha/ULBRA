package AgenciaBancaria;

public class ContaPoupança extends ContaBancaria {

    protected int diaDeRendimento;

    public ContaPoupança(int diaDeRendimento, String cliente, int numConta, float saldo) {
        super(cliente, numConta, saldo);
        this.diaDeRendimento = diaDeRendimento;
    }

    public ContaPoupança(){

    }

    public int getDiaDeRendimento() {
        return diaDeRendimento;
    }

    public void setDiaDeRendimento(int diaDeRendimento) {
        this.diaDeRendimento = diaDeRendimento;
    }

    public void calcularNovoSaldo(int diaAtual, int taxa){
        if (diaAtual >= diaDeRendimento){
            saldo = taxa * saldo;
        }
    }
}
