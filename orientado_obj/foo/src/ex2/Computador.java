package ex2;

public class Computador {

    private String memram;
    private Processador processador;


    public Computador (String memram, Processador processador){
        this.memram = memram;
        this.processador = processador;
    }

    public void detalhes(){
        System.out.println("a ram é"+ getMemram() + " e os detalhes sao " + getProcessador().getMarca() + getProcessador().getMhz());
    }


    public Processador getProcessador() {
        return processador;
    }

    public String getMemram() {
        return memram;
    }
}
