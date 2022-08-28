Casos de teste

Funcionalidade:Fazer cadastro no site buger Eats

Cenario: acessar pagina de cadastro
Dado que esteja na home do site
Quando clicar em "Cadastre-se para fazer entregas"
Entao sou direcionada para a pagina de cadastro


Cenario: Fazer cadastro com dados em branco
Dado que esteja na pagina de cadastro
E preencha os campos com dados em branco
Quando clicar em cadastre-se para fazer entregas
Entao cadastro nao realizado
E sera indicado uma mensagem para informar os dados 

Cenario: Cadastro com dados validos.
Dado que esteja na home do site
E clicar em "Cadastre-se para fazer entregas"
E preencha os campos do formulario com dados validos
E inserir uma imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Entao valido envio dos dados com sucesso

Cenario: Fazer cadastro com CPF invalido e demais campos validos
Dado que esteja na pagina de cadastro
E preencha o campo CPF com dados invalidos
Mas os demais campos com dados validos
Quando clicar em cadastre-se para fazer entregas
Entao cadastro nao enviado
E sera indicado uma mensagen para digitar cpf valido

Cenario: Cadastro com CPF valido e demais campos invalidos.
Dado que esteja na pagina de cadastro
E digite os campos obrigatorios com numeros e caracteres especiais
Mas digite um cpf valido
E inserir uma imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Entao cadastro nao enviado
E sera indicada uma mensagem para inserir um CEP valido.

Cenario: Cadastro com CPF e CEP validos e demais campos invalidos.
Dado que esteja na pagina de cadastro
E digite os campos obrigatorios com numeros e caracteres especiais
E inserir a imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Entao cadastro nao enviado
E sera indicada uma mensagem para inserir "@" no campo e-mail.

Cenario : Cadastro CPF E CEP validos, e-mail e demais campos invalidos
Dado que esteja na pagina de cadastro
E digite os campos obrigatorios com numeros e caracteres especiais
E digite o campo "e-mail" com numeros e caracteres especiais
E insira a imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Entao valido o envio dos dados com sucesso.


Funcionalidade: retornar para a home do site
Cenario: retornar para a home
Dano que esteja na pagina de cadastro
Quanto clicar em voltar para a home
Entao sera direcionado para a home















