import ex1.autor;
import ex1.livro;

static void main(String[] args) {
autor autor = new autor("esfolha", "brasileiro");
livro livro = new livro("o cs2",2000,autor );
livro.descricao();
}