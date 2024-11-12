const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

let messages = []; // Массив для хранения сообщений

app.use(express.static('public'));

io.on('connection', (socket) => {
    console.log('A user connected');

    // Отправка существующих сообщений новому пользователю
    socket.emit('initial messages', messages);

    // Получение нового сообщения
    socket.on('new message', (msg) => {
        const message = { id: Date.now(), text: msg };
        messages.push(message); // Добавляем сообщение в массив
        io.emit('new message', message); // Отправляем сообщение всем пользователям
    });

    // Удаление сообщения
    socket.on('delete message', (id) => {
        messages = messages.filter((message) => message.id !== id); // Удаление сообщения из массива
        io.emit('delete message', id); // Отправка команды на удаление всем пользователям
    });

    socket.on('disconnect', () => {
        console.log('A user disconnected');
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
