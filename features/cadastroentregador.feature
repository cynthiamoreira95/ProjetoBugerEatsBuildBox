# language:pt

Funcionalidade: Como usuario quero preencher o formulario para concluir o cadastro

  @test
Cenário: Fazer cadastro com dados validos
Dado que esteja na home do site
E clicar em "Cadastre-se para fazer entregas"
E preencha os campos do formulario com dados validos
E inserir uma imagem de cnh
Quando clicar em cadastre-se para fazer entregas
Então valido envio dos dados com sucesso