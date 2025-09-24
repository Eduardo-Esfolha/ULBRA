package atividade;

public class Carro {

    private String modelo;
    private int ano ;
    private  String marca;
    private Dono dono;

    public Carro(String modelo, int ano, String marca, Dono dono){
        this.modelo = modelo;
        this.ano = ano;
        this.marca = marca;
        this.dono = dono;
    }

    public Dono getDono() {
        return dono;
    }

    public int getAno() {
        return ano;
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void setDono(Dono dono) {
        this.dono = dono;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
}
