package AgenciaBancaria;

public class ContaEspecial extends ContaBancaria {
    protected float limite;

    public ContaEspecial(String cliente, int numConta, float saldo, float limite) {
        super(cliente, numConta, saldo);
        this.limite = limite;
    }

    public ContaEspecial(){

    }

    public float getLimite() {
        return limite;
    }

    public void setLimite(float limite) {
        this.limite = limite;
    }


    @Override
    public void sacar(float valor){
        float saldoComLimite = getSaldo() + limite;


        if (valor > (saldoComLimite) ){
            System.out.println("saldo insuficiente");

        }else {
            setSaldo(getSaldo() - valor);
        }

    }
}
