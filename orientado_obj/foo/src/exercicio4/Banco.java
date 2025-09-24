package exercicio4;

public class Banco {
        private int conta;
        private String titular;
        private double saldo;

        public Banco (int conta, String titular, double saldo){
            this.conta = conta;
            this.titular = titular;
            this.saldo = saldo;
        }



        public int getConta(){
            return conta;
        }


        public String getTitular(){
            return titular;
        }


        public double getSaldo(){
            return saldo;
        }


        public double depositar(double valor){
            return this.saldo +=valor;

        }


        public double sacar(double valor) {
            if (valor > 0 && valor <= this.saldo){
                this.saldo -= valor;
                return this.saldo;
            }
            else {
                System.out.println("voce nao tem valor para sacar");
            }


            return valor;
        }




    }


