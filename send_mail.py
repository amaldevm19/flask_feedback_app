import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = "smtp.mailtrap.io"
    login = '8153d95809e737'
    password = 'c4821f6f833dd5'
    message = f"<h3>New feedback submission <h3><ul><li>Customer :{customer}</li><li>Dealer :{dealer}</li><li>Rating :{rating}</li><li>Comments :{comments}</li>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'

    msg = MIMEText(message, 'html')
    msg['subject'] = 'Lexus feeback'
    msg['from'] = sender_email
    msg['to'] = receiver_email

    # send email

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
