public class banco {
private int conta = 0101;
private String titular = "esfolha";
private double saldo = 1000;


public int getConta(){
    return conta;
}

public String getTitular(){
    return titular;
    }

public double getSaldo(){
    return saldo;
}

public void depositar( double valor){
    valor = this.saldo + valor;
    System.out.println(valor);
}


}