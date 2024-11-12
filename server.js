// server.js
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Раздаем статику из папки public
app.use(express.static('public'));

// Обработка подключения клиентов
io.on('connection', (socket) => {
    console.log('Новый пользователь подключился');

    // Отправка сообщений
    socket.on('sendMessage', (message) => {
        io.emit('receiveMessage', message);  // Рассылаем всем подключенным
    });

    // Когда клиент отключается
    socket.on('disconnect', () => {
        console.log('Пользователь отключился');
    });
});

// Запуск сервера на порту 3000
server.listen(3000, () => {
    console.log('Сервер работает на порту 3000');
});
