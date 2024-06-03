const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;
const mysql = require('mysql2');

// Middleware para analizar los datos del cuerpo de las solicitudes
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, '/')));

// Ruta para la página de inicio de sesión
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/registrar.html');
});

const dbConfig = {
    host: 'desktop-9f68i6v',
    user: 'root', // reemplazar con el usuario de tu base de datos
    password: 'matz', // reemplazar con la contraseña de tu base de datos
    database: 'tesis' //nombre de la base de datos
};

// Conectar a la base de datos
const connection = mysql.createConnection(dbConfig);

connection.connect((err) => {
    if (err) {
        console.error('Error al conectar a la base de datos: ', err);
        return;
    }
    console.log('Conexión establecida correctamente a la base de datos');
});

// Manejar la solicitud de registro de cuentas
app.post('/register', (req, res) => {
    const { newUsername, newPassword } = req.body;

    // Insertar los datos del nuevo usuario en la base de datos
    const sql = 'INSERT INTO admin (username, password) VALUES (?, ?)';
    connection.query(sql, [newUsername, newPassword], (err, result) => {
        if (err) {
            console.error('Error al insertar datos en la base de datos: ', err);
            res.send('Error al registrar la cuenta');
            return;
        }
        console.log('Registro de cuenta exitoso');
        res.redirect('/inicio.html'); // Redirigir a la página de inicio de sesión
    });
});

// Escuchar en un puerto
app.listen(PORT, () => {
    console.log(`Servidor en ejecución en el puerto ${PORT}`);
});