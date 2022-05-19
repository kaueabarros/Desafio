<h1 align="center">Projeto: Serviço Web – Grafo<h1>
Neste projeto, foi solicitado a criação de um serviço web que disponibilizasse algumas informações a partir de 4 propostas:
  
1.	Uma maneira de expor todos os nós do grafo no estado atual 
2.	Uma maneira de expor todas as pessoas que uma determinada pessoa conhece (nível 1)
3.	Uma maneira de expor todas as pessoas que os amigos daquela pessoa conhece, mas ela não conhece (nível 2)
4.	Uma maneira de cadastrar novas pessoas, informando apenas no cadastro quais são os amigos dela (devolvendo um erro caso algum amigo não exista).

  Para o desenvolvimento deste serviço foram utilizadas as seguintes ferramentas:
<ul> <li>Linguagem de programação:
  <ul>
  <li> Python </li>
  <li> Node.Js </li>
  </ul>
  </ul>
 </ul>
<ul> <li> Bibliotecas utilizadas:
<ul> <li>Python:
  <ul>
<li> Exception</li>
<li> Sys</li>
<li> Json</li>
    </ul>
  </ul>
<ul><li> Node.Js
  <ul>
<li> Express</li>
<li> Cors</li>
    </ul>
  </ul>
  </ul>
  
Foi utilizado como Patterns o modelo MVC por ter um conhecimento melhor nesta metodologia.
Todo o projeto está disponibilizado nas seguintes plataformas:
  <ul><li> GitHub: https://github.com/kaueabarros/Desafio.git</li>
	 <li> DockerHub: https://hub.docker.com/r/kaueabarros/api</li></ul>
 
Foram criadas as seguintes consultas com seus devidos resultados em caso de sucesso e erro:
  <ol> <li>	Uma maneira de expor todos os nós do grafo no estado atual:
    <ul><li>GET: http://<endereço>:3333/listargrafo</li>
      <ul>
<li>Exemplo de retorno com sucesso: {"data": ["Ana", "Maria", "Vinicius", "Luiza", "João", "Carlos"]}</li></li></ul></ul>

<li> Uma maneira de expor todas as pessoas que uma determinada pessoa conhece (nível 1)
<ul><li>GET: http://<endereço>:3333/listaramigos/Nome</li>
  <ul>
<li>Exemplo de retorno com sucesso: {"data": ["Maria", "Vinicius", "Carlos", "João"]}</li>
    <li>Exemplo de retorno com erro: {"error": "Nome não localizado !"}</li></li></ul></ul>

<li> Uma maneira de expor todas as pessoas que os amigos daquela pessoa conhece, mas ela não conhece (nível 2)
<ul><li>GET: http://<endereço>:3333/listarnivel2/Nome</li>
  <ul>
<li>Exemplo de retorno com sucesso: {"data": ["Luiza"]}</li>
<li>Exemplo de retorno com erro: {"error": "Não existe nomes a serem listados"}</li></li></li></ul></ul>

<li> Uma maneira de cadastrar novas pessoas, informando apenas no cadastro quais são os amigos dela (devolvendo um erro caso algum amigo não exista).
<ul><li>GET: http://<endereço>:3333/cadastrarpessoa?pessoa=&amigo=</li>
 
  <table><tr><td>Parâmetros	</td>  </tr>
  <tr><td>pessoa</td>	<td>Nome da pessoa a ser incluída</td></tr>
      <tr><td>amigo</td>	<td>Nome da pessoa já cadastrada</td></tr>
    </table>
  <ul>
<li>Exemplo de retorno com sucesso: {"data": "Nome Adicionado"}</li>
<li>Exemplo de retorno com erro: {"error": "Amigo não localizado !"}</li></li></li></ul></ul>
