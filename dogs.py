import smtplib
from email.mime.text import MIMEText
import requests
from random import randint
from apscheduler.schedulers.blocking import BlockingScheduler

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

username = 'seuemail'
password = 'suasenha'

from_addr = 'seuemail'
to_addrs = ['lista de emails que você quer enviar']

res = requests.get('https://dog.ceo/api/breed/shiba/images')
imgs = res.json()['message']
print(imgs[randint(0, 18)])


def email():
    message = MIMEText(f"<img src='{imgs[randint(0, 18)]}' width='400' height='400'><br> Essa linda imagem foi enviada utilizando Python", 'html', 'utf-8')
    message['subject'] = 'Um dog para você'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
    print('Enviado')

email()

scheduler = BlockingScheduler()
scheduler.add_job(email, 'interval', minutes=1)
scheduler.start()
