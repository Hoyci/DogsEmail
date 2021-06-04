import smtplib
from email.mime.text import MIMEText
import requests
from random import randint


smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465


class DogsMail():
    def __init__(self, username):
        self.username = username
        self.password = 'Sua senha'
        self.to_addrs = []
        self.str_emails = ''
        for i in self.to_addrs:
            self.str_emails += i + ', '
            
        while True:
            emails = input('Insira o email que você deseja enviar: ')

            if emails == '':
                print('Você inseriu um email inválido')
            else:
                self.to_addrs.append(emails)
            
            verification = input('Você deseja adicionar mais emails? ')
            if not verification.upper() == 'S':
                break

    def requisicao(self, raca):
        self.raca = raca
        self.res = requests.get(f'https://dog.ceo/api/breed/{self.raca}/images')
        self.imgs = self.res.json()['message']
        self.arquivo = self.imgs[randint(0, len(self.imgs) - 1)]
        print(self.arquivo)

    def enviar(self):
        try:
            message = MIMEText(f"<img src='{self.arquivo}' width='400' height='400'><br> Essa linda imagem foi enviada utilizando Python", 'html', 'utf-8')
            message['subject'] = 'Um dog para você'
            message['from'] = self.username
            message['to'] = self.str_emails
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(self.username, self.password)
            server.sendmail(self.username, self.to_addrs, message.as_string())
            server.quit()
            print('Enviado')
        except Exception as e:
            print('Erro ao enviar email', e)

email = DogsMail(username='ruan.pablo.drive@gmail.com')
email.requisicao(raca='poodle')
email.enviar()