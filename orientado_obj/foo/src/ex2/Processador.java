package ex2;

public class Processador {
    private  String marca;
    private double mhz;

    public Processador (String marca, double mhz){
        this.marca = marca;
        this.mhz = mhz;

    }


    public String getMarca() {
        return marca;
    }

    public double getMhz() {
        return mhz;
    }


}

