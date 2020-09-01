# SMTP
# Simple Mail transfer protocol

import smtplib

from_email = '@gmail.com'
password = 'abc'
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()  # connect smpt server
conn.starttls()  # start encryption
conn.login(from_email, password)
conn.sendmail(from_email, from_email, 'Subject: So long... \n\n Dear James, \n So long, and thanks for all the fish. \n\n-James')
conn.quit()
