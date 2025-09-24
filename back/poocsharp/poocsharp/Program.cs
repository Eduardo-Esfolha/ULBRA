pessoa pessoa1 = new pessoa("lucas");
pessoa1.idade = 33;
pessoa1.setidade(33);
pessoa1.falar();

pessoa pessoa2 = new pessoa("luana");
pessoa2.idade = 30;
pessoa2.falar();


pessoafisica pf = new pessoafisica();
pf.nome = "andre";
pf.cpf = "12534674";
pf.setidade(33);
pf.falar();
pf.registrar();


pessoajuridica pj = new pessoajuridica();
pj.nome = "loja";
pj.setidade(7);
pj.cnpj = "8329472348";
pj.registrarpj();