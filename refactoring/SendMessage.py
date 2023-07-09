import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendMessage(object):

    def __init__(self, login: str, password: str, host: str, port: int, send_from: str, recipients: list):
        self.login = login
        self.password = password
        self.host = host
        self.port = port
        self.send_to = ', '.join(recipients)
        self.send_from = send_from

    def __enter__(self):
        self.server = smtplib.SMTP(host=self.host, port=self.port)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(self.login, self.password)
        return self

    def send_message(self, message, subject):
        msg = MIMEMultipart(border=';')
        msg['From'] = self.send_from
        msg['To'] = self.send_to
        msg['Subject'] = subject
        msg.attach(MIMEText(message))
        self.server.send_message(msg)

    def __exit__(self, type, value, traceback):
        self.server.quit()
