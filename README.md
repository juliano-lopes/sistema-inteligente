# Sistema Score Inteligente
Projeto para classificação de score de crédito de clientes utilizando modelo de aprendizado de máquina.
## Objetivo  
Este sistema foi desenvolvido para auxiliar sua empresa a determinar com confiança o score de crédito de seus clientes de forma simples e prática por meio de inteligência artificial.  
## Como utilizar  
Para isso, basta baixar o projeto, dar início na API de score inteligente, abrir o arquivo index.html do fronte-end e preencher os campos do formulário com os dados do cliente e clicar em "Obter classificação do score".  
## Construção do modelo  

Acesse o Google Colab para ter acesso ao passo a passo da [construção deste modelo de machine learning](https://colab.research.google.com/drive/19C09evHU5wzetB0mTQZNpPrVRx8NydpV?usp=sharing) utilizado neste sistema de classificação inteligente de score de crédito.  

## Instalação do projeto
* Para poder armazenar grandes arquivos como o pkl do modelo, o projeto utiliza o LFS (Git Large File Storage ).  
* Instale o LFS: **git lfs install**  
* Realize o clone do projeto **git clone https://github.com/juliano-lopes/sistema-inteligente.git**  
* Caso tenha algum problema para utilizar o LFS, [baixe esta versão compactada do projeto](https://drive.google.com/file/d/1nNsNX9KKp--AF37dcPAVKlCTgGhBtrkD/view?usp=sharing) e descompacte em seu computador.  

Após baixar ou realizar o clone deste projeto, siga os passos a seguir:  
* Caso não tenha o python instalado, será necessário instalá-lo em seu sistema;  
* Via linha de comando, entre na pasta raiz do projeto;  
* Instale as dependências do projeto que estão no arquivo "requirementes.txt" com o comando **pip install -r requirements.txt**  
* Entre na pasta "api" e execute os testes com o comando **pytest**  
* Entre na pasta "api" e suba a aplicação com o comando **flask run**  
* Então entre na pasta "front" e abra o arquivo "index.html" e preencha o formulário.  
* Você também pode interagir somente com a API acessando o endereço **http://127.0.0.1:5000** e acessando a documentação do sistema.  

## Conclusão

Dessa maneira é possível utilizar o sistema de classificação inteligente de score de crédito dos seus clientes.