# client.py
import socket
import threading

# Получение сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)  # Выводим сообщение, полученное от сервера
        except:
            break

# Отправка сообщений на сервер
def send_message(client_socket):
    while True:
        message = input()  # Вводим сообщение
        client_socket.send(message.encode('utf-8'))  # Отправляем его на сервер

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))  # Подключаемся к серверу

    # Запрашиваем имя пользователя
    name = input(client_socket.recv(1024).decode('utf-8'))
    client_socket.send(name.encode('utf-8'))  # Отправляем имя на сервер

    # Запуск потоков для получения и отправки сообщений
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_message(client_socket)

if __name__ == "__main__":
    start_client()
