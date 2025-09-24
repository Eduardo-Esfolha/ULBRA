package exercicio5;

public class Retangulo {
private double largura;
private double altura;

public Retangulo (double largura, double altura){
    this.largura = largura;
    this.altura = altura;
}

    public double getAltura() {
        return altura;
    }

    public double getLargura() {
        return largura;
    }

    public void setAltura(double altura) {
        this.altura = altura;
    }

    public void setLargura(double largura) {
        this.largura = largura;
    }

    public double carcularArea(){
        return largura * altura;
    }
}


