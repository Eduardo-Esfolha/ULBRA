import exercicio4.Banco;

public static void main(String[] args) {
    Banco b = new Banco(121, "esfolha", 12);
    b.depositar(10);
    System.out.println(b.getSaldo());
    b.sacar(5);
    System.out.println(b.getSaldo());



}

