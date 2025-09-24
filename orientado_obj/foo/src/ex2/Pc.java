import ex2.Processador;
import ex2.Computador;

void main(String[] args) {
    Processador processador = new Processador("ryzen ", 3.200);
    Computador computador =  new Computador("16gbram", processador);

    computador.detalhes();
}
