#!/bin/bash

# Testar rotas GET
curl -X GET "http://localhost:8000/" -H "Accept: application/json" # Testa a rota GET para a raiz do servidor, deve retornar uma mensagem de boas-vindas ou detalhes da API.
curl -X GET "http://localhost:8000/books" -H "Accept: application/json" # Testa a rota GET para listar todos os livros cadastrados no sistema.
curl -X GET "http://localhost:8000/authors" -H "Accept: application/json" # Testa a rota GET para listar todos os autores cadastrados no sistema.


# Testar rotas POST
curl -X POST "http://localhost:8000/authors" \
    -H "Content-Type: application/json" \
    -d '{"name": "J.R.R. Tolkien", "birthday": 1892, "nationality": "Britânico"}' # Testa a rota POST para criar um novo autor com dados de exemplo.

curl -X POST "http://localhost:8000/books" \
    -H "Content-Type: application/json" \
    -d '{"title": "O Senhor dos Anéis", "genre": "Fantasia", "year": 1954, "author_id": "1"}' # Testa a rota POST para criar um novo livro com dados de exemplo.


# Testar rotas PUT
curl -X PUT "http://localhost:8000/books/1" \
    -H "Content-Type: application/json" \
    -d '{"title": "O Hobbit", "genre": "Fantasia", "year": 1937, "author_id": "1"}' # Testa a rota PUT para atualizar um livro existente com dados atualizados.

curl -X PUT "http://localhost:8000/authors/1" \
    -H "Content-Type: application/json" \
    -d '{"name": "John Ronald Reuel Tolkien", "birthday": 1892, "nationality": "Britânico"}' # Testa a rota PUT para atualizar um autor existente com dados atualizados.

# Testar rotas DELETE
curl -X DELETE "http://localhost:8000/books/1" # Testa a rota DELETE para remover um livro existente identificado pelo ID 1.
curl -X DELETE "http://localhost:8000/authors/1" # Testa a rota DELETE para remover um autor existente identificado pelo ID 1.
