from ReceiveMessage import ReceiveMessage

inbox_args = {
    'login': 'login@gmail.com',
    'password': 'qwerty',
    'server': 'imap.gmail.com',
}


if __name__ == "__main__":
    try:
        with ReceiveMessage(**inbox_args) as search_inbox:
            search_inbox.receive(header=None)
        print('messages collected')
    except Exception as err:
        print(f'Ошибка проверки почты: {err}')
