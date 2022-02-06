# API_Clima_Cidades
Projeto utilizando a biblioteca Tkinter do Python para se informar sobre o clima de uma determinada cidadeno mundo em tempo real por meio de uma API disponível no site https://openweathermap.org

### Ambiente Virtual (crie seu ambiente virtual pelo conda create --name <nome_do_env> ou pelo virtualenv, no meu caso utilizei o conda
`conda activate weather`

### Instale as seguintes bibliotecas com o pip
`pip install tk datetime requests`

### Deploy local
Instale as dependências no **requirements.tx**;
`pip freeze > requirements.txt`

### Funcionalidade da Aplicação
A aplicaçãoexibirá em tela um campo a ser preenchido com um nome de uma cidade , caso digite um nome inválido será exibida uma mensagem pedindo um nome válido

e como output teremos:
* Clima de: (Nome da cidade)
* Temperatura (Celsius):
* Pressão Atmosférica:
* Umidade:
* Hora do Nascer do Sol:
* Hora do Pôr do Sol
* Percentual de Nublado:
* Informações: (chuvoso, nuvens fechadas, ensolarado, céu limpo etc)


