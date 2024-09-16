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
            console.error('Erro ao buscar livros:', error);
        });
}

function fetchAuthors() {
    axios.get('http://localhost:8000/authors')
        .then(response => {
            displayAuthors(response.data);
        })
        .catch(error => {
            console.error('Erro ao buscar autores:', error);
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
    const title = document.getElementById('title').value;
    let genre = document.getElementById('genre').value;
    let year = document.getElementById('year').value;
    let authorId = document.getElementById('author-id').value;

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
        alert('Livro adicionado com sucesso!');
        fetchBooks(); // Atualiza a lista de livros
        clearForm("add-book-form");
    })
    .catch(error => {
        console.error('Erro ao adicionar livro:', error);
    });
}

function addAuthor() {
    const name = document.getElementById('author-name').value;
    let birthday = document.getElementById('birthday').value;
    let nationality = document.getElementById('nationality').value;

    // Se os campos estiverem vazios, defina como null
    birthday = birthday ? birthday : null;
    nationality = nationality ? nationality : null;

    const authorData = {
        name: name, // Campo obrigatório
        birthday: birthday,
        nationality: nationality
    };

    axios.post('http://localhost:8000/authors', authorData)
    .then(response => {
        alert('Autor adicionado com sucesso!');
        fetchAuthors(); // Atualiza a lista de autores
        clearForm("add-author-form");
    })
    .catch(error => {
        console.error('Erro ao adicionar autor:', error);
    });
}

function clearForm(formId) {
    document.getElementById(formId).reset();
}

// Carrega os dados de livros e autores ao iniciar
fetchBooks();
fetchAuthors();
