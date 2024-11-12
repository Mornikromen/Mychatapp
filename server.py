# server.py
import socket
import threading

# Список всех клиентов
clients = []

# Обработка сообщений от клиентов
def handle_client(client_socket):
    client_socket.send('Введите ваше имя: '.encode('utf-8'))  # Запрашиваем имя
    name = client_socket.recv(1024).decode('utf-8')  # Получаем имя клиента
    print(f'Подключился пользователь: {name}')

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(f'{name}: {message}', client_socket)  # Отправляем сообщение всем
            else:
                break
        except:
            clients.remove(client_socket)
            break

# Функция для отправки сообщения всем клиентам
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                continue

# Создаем сервер, который принимает подключения
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Сокет для TCP
    server.bind(('0.0.0.0', 5555))  # Используем все IP адреса и порт 5555
    server.listen(5)  # Максимум 5 клиентов могут подключиться
    print('Сервер запущен, ждем подключения...')

    while True:
        client_socket, addr = server.accept()  # Принимаем подключение
        print(f'Новое подключение от {addr}')
        clients.append(client_socket)  # Добавляем клиента в список
        threading.Thread(target=handle_client, args=(client_socket,)).start()  # Обрабатываем клиента в отдельном потоке

if __name__ == "__main__":
    start_server()
