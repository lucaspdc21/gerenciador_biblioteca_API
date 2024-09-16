// Alterna entre as abas de consulta e cadastro
document.getElementById('consulta-tab').addEventListener('click', function () {
    document.getElementById('consulta-section').classList.remove('d-none');
    document.getElementById('cadastro-section').classList.add('d-none');
    fetchBooks();
    fetchAuthors();
});

document.getElementById('cadastro-tab').addEventListener('click', function () {
    document.getElementById('cadastro-section').classList.remove('d-none');
    document.getElementById('consulta-section').classList.add('d-none');
});

// Funções para carregar dados e manipulação da API
function fetchBooks() {
    axios.get('http://localhost:8000/books')
        .then(response => {
            displayBooks(response.data);
        })
        .catch(error => {
            alert('Erro ao buscar livros: ' + error);
        });
}

function fetchAuthors() {
    axios.get('http://localhost:8000/authors')
        .then(response => {
            displayAuthors(response.data);
        })
        .catch(error => {
            alert('Erro ao buscar autores: ' + error);
        });
}

function displayBooks(data) {
    const resultsDiv = document.getElementById('books-response');
    let table = '<table class="table table-striped"><thead><tr><th>ID</th><th>Título</th><th>Gênero</th><th>Ano</th><th>ID do Autor</th></tr></thead><tbody>';
    for (const id in data) {
        const book = data[id];
        table += `<tr>
                    <td>${id}</td>
                    <td>${book.title}</td>
                    <td>${book.genre}</td>
                    <td>${book.year}</td>
                    <td>${book.author_id}</td>
                  </tr>`;
    }
    table += '</tbody></table>';
    resultsDiv.innerHTML = table;
}

function displayAuthors(data) {
    const resultsDiv = document.getElementById('authors-response');
    let table = '<table class="table table-striped"><thead><tr><th>ID</th><th>Nome</th><th>Livros</th><th>Aniversário</th><th>Nacionalidade</th></tr></thead><tbody>';
    for (const id in data) {
        const author = data[id];
        let books = '';
        for (const bookId in author.books) {
            const book = author.books[bookId];
            books += `${book.title} (${book.year}), `;
        }
        books = books.slice(0, -2); // Remove a última vírgula e espaço
        table += `<tr>
                    <td>${id}</td>
                    <td>${author.name}</td>
                    <td>${books}</td>
                    <td>${author.birthday}</td>
                    <td>${author.nationality}</td>
                  </tr>`;
    }
    table += '</tbody></table>';
    resultsDiv.innerHTML = table;
}

function addBook() {
    const title = document.getElementById('title-add-book').value;
    let genre = document.getElementById('genre-add-book').value;
    let year = document.getElementById('year-add-book').value;
    let authorId = document.getElementById('author-id-add-book').value;

    // Se os campos estiverem vazios, defina como null
    genre = genre ? genre : null;
    year = year ? parseInt(year) : null;
    authorId = authorId ? authorId : null;

    const bookData = {
        title: title, // Campo obrigatório
        genre: genre,
        year: year,
        author_id: authorId
    };

    axios.post('http://localhost:8000/books', bookData)
    .then(response => {
        alert('Livro adicionado com sucesso!\nID do livro: ' + response.data);
        fetchBooks(); // Atualiza a lista de livros
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("add-book-form");
    })
    .catch(error => {
        alert('Erro ao adicionar livro: ' + error);
    });
}

function addAuthor() {
    const name = document.getElementById('author-name-add-author').value;
    let birthday = document.getElementById('birthday-add-author').value;
    let nationality = document.getElementById('nationality-add-author').value;

    // Se os campos estiverem vazios, define como null
    birthday = birthday ? birthday.split('-').reverse().join('/') : null;
    nationality = nationality ? nationality : null;

    const authorData = {
        name: name, // Campo obrigatório
        birthday: birthday,
        nationality: nationality
    };

    axios.post('http://localhost:8000/authors', authorData)
    .then(response => {
        alert('Autor adicionado com sucesso!\nID do autor: ' + response.data);
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("add-author-form");
    })
    .catch(error => {
        alert('Erro ao adicionar autor: ' + error);
    });
}

function updateBook() {
    const bookId = document.getElementById('book-id-update-book').value;
    const title = document.getElementById('title-update-book').value;
    let genre = document.getElementById('genre-update-book').value;
    let year = document.getElementById('year-update-book').value;
    let authorId = document.getElementById('author-id-update-book').value;
    
    // Se os campos estiverem vazios, define como null
    genre = genre ? genre : null;
    year = year ? parseInt(year) : null;
    authorId = authorId ? authorId : null;

    const bookData = {
        title: title, // Campo obrigatório
        genre: genre,
        year: year,
        author_id: authorId
    };

    axios.put('http://localhost:8000/books/' + bookId, bookData)
    .then(response => {
        alert('Livro atualizado com sucesso!');
        fetchBooks(); // Atualiza a lista de livros
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("update-book-form");
    })
    .catch(error => {
        alert('Erro ao atualizar livro: ' + error);
    });
}

function updateAuthor() {
    const authorId = document.getElementById('author-id-update-author').value;
    const name = document.getElementById('author-name-update-author').value;
    let birthday = document.getElementById('birthday-update-author').value;
    let nationality = document.getElementById('nationality-update-author').value;

    // Se os campos estiverem vazios, define como null
    birthday = birthday ? parseInt(birthday) : null;
    nationality = nationality ? nationality : null;

    const authorData = {
        name: name, // Campo obrigatório
        birthday: birthday,
        nationality: nationality
    };

    axios.put('http://localhost:8000/authors/' + authorId, authorData)
    .then(response => {
        alert('Autor atualizado com sucesso!');
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("update-author-form");
    })
    .catch(error => {
        alert('Erro ao atualizar autor: ' + error);
    });
}

function addAssociation() {
    const book_id = document.getElementById('book-id-add-association').value; // Campo obrigatório
    const author_id = document.getElementById('author-id-add-association').value // Campo obrigatório

    axios.post('http://localhost:8000/authors/' + author_id + '/books/' + book_id)
    .then(response => {
        alert('Associação criada com sucesso!');
        fetchBooks(); // Atualiza a lista de livros
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("add-association-form");
    })
    .catch(error => {
        alert('Erro ao criar associação: ' + error)
    });
}

function deleteAssociation() {
    const book_id = document.getElementById('book-id-delete-association').value; // Campo obrigatório
    const author_id = document.getElementById('author-id-delete-association').value // Campo obrigatório

    axios.delete('http://localhost:8000/authors/' + author_id + '/books/' + book_id)
    .then(response => {
        alert('Associação deletada com sucesso!');
        fetchBooks(); // Atualiza a lista de livros
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("delete-association-form");
    })
    .catch(error => {
        alert('Erro ao deletar associação: ' + error)
    });
}

function deleteBook() {
    const id = document.getElementById('book-id-delete-book').value; // Campo obrigatório
    
    axios.delete('http://localhost:8000/books/' + id)
    .then(response => {
        alert('Livro deletado com sucesso!');
        fetchBooks(); // Atualiza a lista de livros
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("delete-book-form");
    })
    .catch(error => {
        alert('Erro ao deletar livro: ' + error)
    });
}

function deleteAuthor() {
    const id = document.getElementById('author-id-delete-author').value; // Campo obrigatório

    axios.delete('http://localhost:8000/authors/' + id)
    .then(response => {
        alert('Autor deletado com sucesso!');
        fetchBooks(); // Atualiza a lista de livros
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("delete-author-form");
    })
    .catch(error => {
        alert('Erro ao deletar autor: ' + error);
    });
}

function clearForm(formId) {
    document.getElementById(formId).reset();
}

// Carrega os dados de livros e autores ao iniciar
fetchBooks();
fetchAuthors();
