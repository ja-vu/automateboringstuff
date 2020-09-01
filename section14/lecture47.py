# IMAP
# Internet Message Access Protocol

import imapclient
import datetime
import pyzmail

email = '@gmail.com'
password = 'abc'

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login(email, password)
conn.select_folder('INBOX', readonly=True)
UIDs = conn.search([u'SINCE', datetime.date(2020,8,20)])
print(UIDs)
rawMessage = conn.fetch([26731], ['BODY[]', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[26731][b'BODY[]'])
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))
print(message.get_addresses('bcc'))
print(message.text_part)
print(message.html_part == None)
print(message.text_part.get_payload().decode('UTF-8'))
print(message.text_part.charset == None)
print(conn.list_folders())

# To Delete an email
conn.select_folder('INBOX', readonly=False)
UIDs = conn.search([u'SINCE', datetime.date(2020,8,20)])
conn.delete_messages([26731])
