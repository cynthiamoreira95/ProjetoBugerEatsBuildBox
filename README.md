### AUTOMAÇÃO BUGER EATS

O critério decisivo para esta automação foi um caso de teste positivo onde o cadastro é
enviado para avaliação com sucesso. Utilizei a linguagem Python para este projeto.

A documentação não foi disponibilizada para este projeto, então realizei um teste exploratório para confirmar quais
dados eram obrigatórios. Sendo eles: *nome*, *cpf*, *e-mail*, *whatsapp*, *cep*, *número da residência*,*método de 
entrega* e *foto da cnh*. 

O BDD foi gerado através da library Behave, onde o passo a passo do teste foi inserido em *Steps*. 
Para controle do navegador, utilizei o *Selenium WebDriver*, e o setup do navegador está na class *Browser*.
Os métodos para execução estão na class *Utils* por questão de organização. Os métodos de preenchimento de dados são
reutilizáveis.
Para o upload do arquivo, optei pela library *Pyautogui*, que manipula mouse e teclado. É recomendado que para executar 
este step, faça o download da imagem que estará na pasta *images* e salve exatamente com o mesmo nome (CNH.JPG). No
momento da execução, não mexa no mouse ou teclado, pois o código fará o click por posição. A resolução de tela para 
obter êxito na execução é *1355 x 768*.
Os cenários foram validados através do *Nose*, onde o botão "Fechar" foi o parâmetro de asserção, pois só aparece após
envio dos dados solicitados.