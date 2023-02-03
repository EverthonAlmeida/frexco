# frexco
Repositório para o teste de Estpagio da Frexco sobre Previsão de Vendas.

### Configuração do ambiente virtual

Antes de instalar as dependências, sugiro criar um ambiente virtual. Sendo necessário instalar o pacote `virtualenvwrapper`, através do comando:
```
pip install virtualenvwrapper
```
Após isso, crie seu ambiente virtual com o comando:
```
mkvirtualenv [nome do ambiente]
```
Documentação completa do `virtualenvwrapper` nesse [link](https://virtualenvwrapper.readthedocs.io/en/latest/index.html).

### Instalação das dependências

Para instalar as dependências do Script, utilize o comando:
```
pip install -r requirements.txt
```

## Execução

Para executar o Script, execute o comando:
```
python3 script.py
```
Será aberta uma aba em seu navegador contendo o gráfico que ilustra a previsão de vendas do ítem para os próximos 5 dias, partindo da última data descrita na planilha 'Dados.xlsx'.
