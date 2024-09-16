#!/bin/bash

# Testar rotas GET
echo "TESTANDO ROTAS GET"
# GET na raiz
echo "---------------------------------
Raiz do servidor: localhost:8000/
"
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i # Testa a rota GET para a raiz do servidor

# GET nos livros
echo "
---------------------------------
Livros: localhost:8000/books
"
curl -X GET "http://localhost:8000/books" -H "Accept: application/json" -i # Testa a rota GET para listar todos os livros cadastrados no sistema.

# GET nos autores
echo "
---------------------------------
Autores: localhost:8000/authors
"
curl -X GET "http://localhost:8000/authors" -H "Accept: application/json" -i # Testa a rota GET para listar todos os autores cadastrados no sistema.




# Testar rotas POST
# Testa a rota POST para criar um novo livro com dados de exemplo.
echo "

TESTANDO ROTAS POST"
echo "---------------------------------
Criando livro: POST localhost:8000/books
(senhor dos anéis, fantasia, 1954)
"
curl -X POST "http://localhost:8000/books" -i \
     -H "Content-Type: application/json" \
     -d '{"title": "O Senhor dos Anéis", "genre": "Fantasia", "year": 1954}'


# Testa a rota POST para criar um novo autor com dados de exemplo.
echo "
---------------------------------
Criando autor: POST localhost:8000/authors
(J.R.R. Tolkien, 1892, Britânico)
"
curl -X POST "http://localhost:8000/authors" -i \
     -H "Content-Type: application/json" \
     -d '{"name": "J.R.R. Tolkien", "birthday": 1892, "nationality": "Britânico"}'

# Testa a rota POST para linkar um livro com um autor
echo "
---------------------------------
Criando link entre autor e livro: POST localhost:8000/authors/1/books/1
"
curl -X POST "http://localhost:8000/authors/1/books/1" -i \




# Testar rotas GET
echo "

TESTANDO ROTAS GET"
echo "---------------------------------
Raiz do servidor até o momento: GET localhost:8000/
"
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i


echo "---------------------------------
Listando todos os livros de um autor específico: GET localhost:8000/authors/1/books
"
curl -X GET "http://localhost:8000/authors/1/books" -H "Accept: application/json" -i




# Testar rotas PUT
# Testa a rota PUT para atualizar um livro existente com dados atualizados.
echo "

TESTANDO ROTAS PUT"
echo "
---------------------------------
Editando livro de ID 1: PUT localhost:8000/books/1
(O Hobbit, Fantasia, 1937, author_id 1)
"
curl -X PUT "http://localhost:8000/books/1" -i \
    -H "Content-Type: application/json" \
    -d '{"title": "O Hobbit", "genre": "Fantasia", "year": 1937, "author_id": "1"}'

# Testa a rota PUT para atualizar um autor existente com dados atualizados.
echo "
---------------------------------
Editando autor de ID 1: PUT localhost:8000/authors/1
(John Ronald Reuel Tolkien, 1892, Britânico)
"
curl -X PUT "http://localhost:8000/authors/1" -i \
    -H "Content-Type: application/json" \
    -d '{"name": "John Ronald Reuel Tolkien", "birthday": 1892, "nationality": "Britânico"}'



# Testar rotas GET
echo "

TESTANDO ROTAS GET"
echo "---------------------------------
Raiz do servidor após a edição: GET localhost:8000/
"
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i




# Testar rotas DELETE
echo "

TESTANDO ROTAS DELETE"
echo "---------------------------------
Deletando o link entre o autor 1 e o livro 1: DELETE localhost:8000/authors/1/books/1
"
curl -X DELETE "http://localhost:8000/authors/1/books/1" -i # Testa a rota DELETE para remover o link entre um livro e um autor




echo "
---------------------------------
Raiz do servidor após a deleção: GET localhost:8000/
"
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i



# Testa a rota DELETE para remover um livro existente identificado pelo ID 1.
echo "
---------------------------------
Deletando o livro 1: DELETE localhost:8000/books/1
"
curl -X DELETE "http://localhost:8000/books/1" -i

# Testa a rota DELETE para remover um autor existente identificado pelo ID 1.
echo "
---------------------------------
Deletando o autor 1: DELETE localhost:8000/authors/1
"
curl -X DELETE "http://localhost:8000/authors/1" -i



echo "---------------------------------
Raiz do servidor após a deleção: GET localhost:8000/
"
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i