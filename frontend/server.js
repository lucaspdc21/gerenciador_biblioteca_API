const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

// Serve arquivos estáticos da pasta 'src'
app.use(express.static(path.join(__dirname, 'src')));

// Inicia o servidor
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
