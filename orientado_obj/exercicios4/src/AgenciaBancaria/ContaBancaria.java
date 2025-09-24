package AgenciaBancaria;

public class ContaBancaria {
    protected String cliente;
    protected int numConta;
    protected float saldo;


    public ContaBancaria(String cliente, int numConta, float saldo) {
        this.cliente = cliente;
        this.numConta = numConta;
        this.saldo = saldo;
    }

    public ContaBancaria(){

    }

    public String getCliente() {
        return cliente;
    }

    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

    public int getNumConta() {
        return numConta;
    }

    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }

    public float getSaldo() {
        return saldo;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public void sacar(float valor){
        if (valor > 0 && valor > saldo){
            System.out.println("valor nao pode ser sacado");
        }
        saldo = saldo - valor;
    }

    public void depositar(float valor){
        if (valor < 0 ){
            System.out.println("valor nao pode ser depostitado");
        }
        saldo =+valor;

    }
}


