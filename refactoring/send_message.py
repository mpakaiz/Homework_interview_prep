from SendMessage import SendMessage

send_args = {
    'login': 'login@gmail.com',
    'password': 'qwerty',
    'host': 'smtp.gmail.com',
    'port': 587,
    'send_from': 'login@gmail.com',
    'send_to': ['vasya@email.com', 'petya@email.com']
}

if __name__ == "__main__":
    try:
        with SendMessage(**send_args) as email_host:
            email_host.send_message(message='Message', subject='Subject')
        print('Message Send')
    except Exception as err:
        print(f'Ошибка отправки сообщения: {err}')
