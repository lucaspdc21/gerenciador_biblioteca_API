# Projeto de API Biblioteca
Uma simples API REST, capaz de gerenciar alguns elementos de uma biblioteca e um frontend capaz de consumir essa API possibilitando testar o servico.

[Relatório do projeto](https://docs.google.com/document/d/1LCVqZfnoafkD_5QALPn5PptOE0VVdfd0bvBkuZ-iBMw/edit?usp=sharing)

## Estrutura do Projeto
- **API(Server)**: Desenvolvido em Python, utilizando os módulos http e urllib
- **Front-end**: Implementado com Node, utilizando JavaScript, CSS e HTML para criar uma interface web que interage com a API.
---
## API

O projeto foi organizado seguindo o padrão mvc, dentro da pasta `/server` é possível encontrar as pastas: 
- `/model`: Contém as classes das entidades book e author
- `/controller`: Contém os arquivos relacionados ao RequestHandler e o arquivo controller, que contém os dicionários onde as entidades criadas são salvas, bem como os métodos usados para gerenciar as mesmas
- `main.py`: Contém os códigos necessários para iniciar o servidor 

## Como Executar o Projeto
### API
#### Opção 1:
Execute o script shell `run_server.sh`
#### Opção 2: (Manual)
1. Navegue até a pasta server
```bash
cd server
```
2. Execute o código main.py
```bash
python main.py
```
3. Após isso o servidor será iniciado na porta `localhost:8000`

### Front-end

1. Para executar o frontend é necessário ter o node instalado em sua máquina, consulte a documentação [aqui](https://nodejs.org/en/download/package-manager)
2. Navegue até a pasta server
```bash
cd frontend
```
3. Instale as dependências necessárias
```bash
npm install
```
4. Execute
```bash
node server.js
```
5. O frontend será aberto na porta `localhost:3000`

Após a instalação das dependências também é possível executar o script shell `run_frontend.sh`
# Documentação da API
https://app.swaggerhub.com/apis-docs/LucasPinheiro/Library_API/1.0.0#/
