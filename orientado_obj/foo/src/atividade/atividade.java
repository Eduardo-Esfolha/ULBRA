import atividade.Carro;
import atividade.Dono;

public static  void main(String[] args) {
Dono dono = new Dono("esfolha","56768785");
Carro carro =  new Carro("onix", 2019, "chevrolet", dono);

    System.out.println(" o carro: " + carro.getModelo() + " esta vinculado ao cpf:" + carro.getDono().getCpf());
}
