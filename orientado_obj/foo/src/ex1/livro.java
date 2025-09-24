package ex1;


public class livro {
    private String titulo;
    private int anopublicacao;
    private autor autor;

    public livro(String titulo, int anopublicacao, autor autor){
        this.titulo = titulo;
        this.anopublicacao = anopublicacao;
        this.autor = autor;

    }

public void descricao(){
    System.out.println(getTitulo()+ getAutor().getNome());

}


    public autor getAutor() {
        return autor;
    }

    public int getAnopublicacao() {
        return anopublicacao;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setAnopublicacao(int anopublicacao) {
        this.anopublicacao = anopublicacao;
    }

    public void setAutor(autor autor) {
        this.autor = autor;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
}
