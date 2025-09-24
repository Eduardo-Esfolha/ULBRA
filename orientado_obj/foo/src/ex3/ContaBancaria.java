package ex3;

public class ContaBancaria {
    private int numeroConta;
    private  double saldo;
    private Cliente cliente;

    public ContaBancaria(int numeroConta, double saldo , Cliente cliente){
        this.numeroConta = numeroConta;
        this.saldo = saldo;
        this.cliente = cliente;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public int getNumeroConta() {
        return numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }


    public void depositar(double valor){
        if (valor > 0){
              saldo+= valor;
        }else {
            System.out.println("valor nao disponivel");
        }


    }

    public void sacar(double valor){
        if (valor <= saldo && valor > 0 ){
            saldo = saldo - valor;
    }else {
            System.out.println("valor impossivel para sacar");
        }
        }
}


