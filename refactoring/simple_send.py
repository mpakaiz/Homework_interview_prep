from SendMessage import SendMessage

gmail_SMTP = "smtp.gmail.com"
port = 587
login = 'login@gmail.com'
password = 'qwerty'
subject = 'Subject'
recipients = ['vasya@email.com', 'petya@email.com']
message = 'Message'


if __name__ == "__main__":

    send_message = SendMessage(login, password, gmail_SMTP, port, login, recipients)
    send_message.send_message(message, subject)
