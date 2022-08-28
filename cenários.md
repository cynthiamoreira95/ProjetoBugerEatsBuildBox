OBS: cenarios de teste escritos com base em que foram 
feitos testes unitarios em cada campo. Teste de análise de valor limite não foi considerado, pois são realizados em testes unitários.





Funcionalidade:Fazer cadastro no site buger Eats

Cenario: acessar pagina de cadastro
Dado que esteja na home do site
Quando clicar em "Cadastre-se para fazer entregas"
Então sou direcionado para a pagina de cadastro


Cenario: Fazer cadastro com dados em branco
Dado que esteja na pagina de cadastro
E preencha os campos com dados em branco
Quando clicar em cadastre-se para fazer entregas
Entao cadastro nao realizado
E sera indicado uma mensagem para informar os dados 
Cenário: Preencher campos com letra, números e caractéres especiais.

Cenário: Cadastro com dados válidos.
Dado que esteja na home do site
E clicar em "Cadastre-se para fazer entregas"
E preencha os campos do formulario com dados validos
E inserir uma imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Então valido envio dos dados com sucesso

Cenario: Fazer cadastro com CPF inválido e demais campos validos
Dado que esteja na pagina de cadastro
E preencha o campo CPF com dados invalidos
Mas os demais campos com dados válidos
Quando clicar em cadastre-se para fazer entregas
Entao cadastro nao enviado
E sera indicado uma mensagen para digitar cpf válido

Cenário: Cadastro com CPF válido e demais campos invalidos.
Dado que esteja na página de cadastro
E digite os campos obrigatórios com números e caracteres especiais
Mas digite um cpf válido
E inserir uma imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Então cadastro não enviado
E será indicada uma mensagem para inserir "@" no campo e-mail

Cenário: Cadastro com CPF e CEP válidos e demais campos inválidos.
Dado que esteja na página de cadastro
E digite os campos obrigatórios com números e caracteres especiais
E inserir a imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Então cadastro não enviado
E será indicada uma mensagem para inserir "@" no campo e-mail.

Cenário : Cadastro CPF E CEP válidos, e demais campos inválidos
Dado que esteja na pagina de cadastro
E digite os campos obrigatórios com numeros e caracteres especiais
E digite o campo "e-mail" com números e caracteres especiais
E insira a imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Então valido o envio dos dados com sucesso.


Funcionalidade: retornar para a home do site
Cenario: retornar para a home
Dano que esteja na pagina de cadastro
Quanto clicar em voltar para a home
Entao sera direcionado para a home















