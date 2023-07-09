from ReceiveMessage import ReceiveMessage

gmail_IMAP = "imap.gmail.com"
login = 'login@gmail.com'
password = 'qwerty'
header = None


if __name__ == "__main__":
    receive_message = ReceiveMessage(login, password, gmail_IMAP)
    receive_message.receive(header)
