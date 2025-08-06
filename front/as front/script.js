function verform(){
    document.getElementById('form').style.display='block'
}

function naover(){
    document.getElementById('form').style.display='none'
}

let ex = []
let ex_ok = []
const form = document.getElementById("form")
const tabela = document.getElementById("tabela")
const tabelaok = document.getElementById("tabelaok")
const nome = document.getElementById("nome")
const series = document.getElementById("serie")
const rept = document.getElementById("rept")
form.addEventListener("submit", function (e){
    e.preventDefault()
    ex.push([nome.value, series.value, rept.value])
    nome.value = "";
    series.value = "";
    rept.value = "";
    addtabela()


})

function addtabela() {
  tabela.innerHTML = `
    <tr>
      <th>nome</th>
      <th>series</th>
      <th>repetições</th>
      <th>concluir</th>
      <th>remover</th>
    </tr>
  `;
  
  ex.forEach((element, index) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${element[0]}</td>
      <td>${element[1]}</td>
      <td>${element[2]}</td>
      <td><button onclick="concluir(${index})">✔️</button></td>
      <td><button onclick="remover(${index})">🗑️</button></td>
    `;
    tabela.appendChild(tr);
  });

}

function concluir(index) {
    ex_ok.push(ex[index]);
    ex.splice(index, 1);
    addtabela();
    addtabelaok();
}


function remover(index) {
    ex_ok.splice(index, 1);
    ex.splice(index, 1);
    addtabela();
    
}

function addtabelaok() {
  tabelaok.innerHTML = `
    <tr>
      <th>nome</th>
      <th>series</th>
      <th>repetições</th>
    </tr>
  `;
  
  ex_ok.forEach((element, index) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${element[0]}</td>
      <td>${element[1]}</td>
      <td>${element[2]}</td>
    `;
    tabelaok.appendChild(tr);
  });
}
