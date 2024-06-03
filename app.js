const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;
const mysql = require('mysql2');
const dbConfig = {
    host: 'desktop-9f68i6v',
    user: 'root', //reemplazar con el usuario de tu base de datos
    password: 'matz', //reemplazar con la contraseña de tu base de datos
    database: 'nombre_de_la_base_de_datos'
};

// Middleware para analizar los datos del cuerpo de las solicitudes
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, 'public')));

// Ruta para la página de inicio de sesión
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/inicio.html');
});

// Ruta para manejar el inicio de sesión
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    // Validar el usuario y la contraseña (solo un ejemplo, debes implementar la lógica de autenticación real)
    if (username === 'hola' && password === 'wa') {
        // Redirigir al usuario a la página de inicio o hacer cualquier otra acción necesaria
        res.redirect('/home.html');
    } else {
        // Si las credenciales son incorrectas, redirigir al usuario de vuelta al formulario de inicio de sesión con un mensaje de error
        res.send('Credenciales incorrectas');
    }
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor en ejecución en el puerto ${PORT}`);
});