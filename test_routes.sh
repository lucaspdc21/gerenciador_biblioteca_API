#!/bin/bash

# Testar rotas GET
echo "TESTANDO ROTAS GET"
# GET na raiz
echo "---------------------------------
Raiz do servidor: GET localhost:8000/
"
read
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i # Testa a rota GET para a raiz do servidor

# GET nos livros
echo "
---------------------------------
Livros: GET localhost:8000/books
"
read
curl -X GET "http://localhost:8000/books" -H "Accept: application/json" -i # Testa a rota GET para listar todos os livros cadastrados no sistema.

# GET nos autores
echo "
---------------------------------
Autores: GET localhost:8000/authors
"
read
curl -X GET "http://localhost:8000/authors" -H "Accept: application/json" -i # Testa a rota GET para listar todos os autores cadastrados no sistema.

# GET nos autores
echo "
---------------------------------
Pasta inexistente: GET localhost:8000/asdasd
"
read
curl -X GET "http://localhost:8000/asdasd" -H "Accept: application/json" -i # Testa a rota GET em pasta inexistente




# Testar rotas POST
# Testa a rota POST para criar um novo livro com dados de exemplo.
printf "\n\nTESTANDO ROTAS POST\n"
echo "---------------------------------
Criando livro: POST localhost:8000/books
(senhor dos anéis, fantasia, 1954)
"
read
curl -X POST "http://localhost:8000/books" -i \
     -H "Content-Type: application/json" \
     -d '{"title": "O Senhor dos Anéis", "genre": "Fantasia", "year": 1954}'


# Testa a rota POST para criar um novo autor com dados de exemplo.
echo "
---------------------------------
Criando autor: POST localhost:8000/authors
(J.R.R. Tolkien, 03/01/1892, Britânico)
"
read
curl -X POST "http://localhost:8000/authors" -i \
     -H "Content-Type: application/json" \
     -d '{"name": "J.R.R. Tolkien", "birthday": "03/01/1892", "nationality": "Britânico"}'

echo "---------------------------------
Criando livro com author_id inválido: POST localhost:8000/books
(Moby Dick, Aventura, 1851, 2)
"
read
curl -X POST "http://localhost:8000/books" -i \
     -H "Content-Type: application/json" \
     -d '{"title": "Moby Dick", "genre": "Aventura", "year": 1851, "author_id": "2"}'

# Testa a rota POST para linkar um livro com um autor
echo "
---------------------------------
Criando link entre autor e livro: POST localhost:8000/authors/1/books/1
"
read
curl -X POST "http://localhost:8000/authors/1/books/1" -i \

# Testa a rota POST para linkar um livro com um autor inexistente
echo "
---------------------------------
Tentando criar link entre autor inexistente e livro: POST localhost:8000/authors/2/books/1
"
read
curl -X POST "http://localhost:8000/authors/2/books/1" -i \

# Testa a rota POST para criar um link que já existe
echo "
---------------------------------
Tentando criar link já existente entre autor e livro: POST localhost:8000/authors/1/books/1
"
read
curl -X POST "http://localhost:8000/authors/1/books/1" -i \


# Testar rotas GET
printf "\n\nTESTANDO ROTAS GET\n"
echo "---------------------------------
Raiz do servidor até o momento: GET localhost:8000/ 
"
read
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i


echo "
---------------------------------
Listando todos os livros de um autor específico: GET localhost:8000/authors/1/books
"
read
curl -X GET "http://localhost:8000/authors/1/books" -H "Accept: application/json" -i




# Testar rotas PUT
# Testa a rota PUT para atualizar um livro existente com dados atualizados.
printf "\n\nTESTANDO ROTAS PUT\n"
echo "---------------------------------
Editando livro de ID 1: PUT localhost:8000/books/1
(O Hobbit, Fantasia, 1937, author_id 1)
"
read
curl -X PUT "http://localhost:8000/books/1" -i \
    -H "Content-Type: application/json" \
    -d '{"title": "O Hobbit", "genre": "Fantasia", "year": 1937, "author_id": "1"}'

# Testa a rota PUT para atualizar um autor existente com dados atualizados.
echo "
---------------------------------
Editando autor de ID 1: PUT localhost:8000/authors/1
(John Ronald Reuel Tolkien, 03/01/1892, Britânico)
"
read
curl -X PUT "http://localhost:8000/authors/1" -i \
    -H "Content-Type: application/json" \
    -d '{"name": "John Ronald Reuel Tolkien", "birthday": "03/01/1892", "nationality": "Britânico"}'

echo "
---------------------------------
Tentando editar autor de ID 1 com dados inválidos: PUT localhost:8000/authors/1
(John Ronald Reuel Tolkien, banana, Britânico)
"
read
curl -X PUT "http://localhost:8000/authors/1" -i \
    -H "Content-Type: application/json" \
    -d '{"name": "John Ronald Reuel Tolkien", "birthday": "banana", "nationality": "Britânico"}'

echo "
---------------------------------
Tentando editar autor de ID 1 com JSON quebrado: PUT localhost:8000/authors/1
(John Ronald Reuel Tolkien, 03/01/1892 Britânico)
(foram retiradas algumas aspas e vírgulas)
"
read
curl -X PUT "http://localhost:8000/authors/1" -i \
    -H "Content-Type: application/json" \
    -d '{"name": John Ronald Reuel Tolkien", "birthday": "banana" "nationality": "Britânico"}'

# Testar rotas GET
printf "\n\nTESTANDO ROTAS GET\n"
echo "---------------------------------
Raiz do servidor após a edição: GET localhost:8000/
"
read
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i




# Testar rotas DELETE
printf "\n\nTESTANDO ROTAS DELETE\n"
echo "---------------------------------
Deletando o link entre o autor 1 e o livro 1: DELETE localhost:8000/authors/1/books/1
"
read
curl -X DELETE "http://localhost:8000/authors/1/books/1" -i # Testa a rota DELETE para remover o link entre um livro e um autor


echo "
---------------------------------
Tentando deletar o link inexistente entre o autor 1 e o livro 1: DELETE localhost:8000/authors/1/books/1
"
read
curl -X DELETE "http://localhost:8000/authors/1/books/1" -i # Testa a rota DELETE para remover o link entre um livro e um autor



echo "
---------------------------------
Raiz do servidor após a deleção: GET localhost:8000/
"
read
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i



# Testa a rota DELETE para remover um livro existente identificado pelo ID 1.
echo "
---------------------------------
Deletando o livro 1: DELETE localhost:8000/books/1
"
read
curl -X DELETE "http://localhost:8000/books/1" -i

# Testa a rota DELETE para remover um autor existente identificado pelo ID 1.
echo "
---------------------------------
Deletando o autor 1: DELETE localhost:8000/authors/1
"
read
curl -X DELETE "http://localhost:8000/authors/1" -i

# Testa a rota DELETE para remover um autor existente identificado pelo ID 1.
echo "
---------------------------------
Tentando deletar o autor 1 novamente: DELETE localhost:8000/authors/1
"
read
curl -X DELETE "http://localhost:8000/authors/1" -i

# Testa a rota DELETE para remover um autor existente identificado pelo ID 1.
echo "
---------------------------------
Tentando deletar a pasta books: DELETE localhost:8000/books
"
read
curl -X DELETE "http://localhost:8000/books" -i



echo "---------------------------------
Raiz do servidor após a deleção: GET localhost:8000/
"
read
curl -X GET "http://localhost:8000/" -H "Accept: application/json" -i