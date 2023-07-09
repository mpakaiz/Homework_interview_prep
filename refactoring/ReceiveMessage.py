import email
import imaplib


class ReceiveMessage(object):

    def __init__(self, login, password, server):
        self.login = login
        self.password = password
        self.box = imaplib.IMAP4_SSL(server)
        self.box.login(self.login, self.password)
        print("logged in")
        self.box.list()
        self.box.select('inbox')
        print('Inbox selected')

    # def __enter__(self):
    #     self.box.login(self.login, self.password)
    #     print("logged in")
    #     self.box.list()
    #     self.box.select('inbox')
    #     print('Inbox selected')

    def receive(self, header):
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = self.box.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = self.box.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        self.box.logout()
        return email_message
