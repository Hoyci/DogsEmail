import smtplib
from email.mime.text import MIMEText
import requests
from random import randint


smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465


class DogsMail():
    def __init__(self, username, password):
        self.username = username
        self.password = password
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

    def requisicao(self, raca=None, subraca=None):
        if raca==None and subraca==None:
            self.res = requests.get(f'https://dog.ceo/api/breeds/image/random')
            self.img = self.res.json()['message']
            self.arquivo = self.img
            print(self.arquivo)
        elif subraca==None:
            self.raca = raca
            self.res = requests.get(f'https://dog.ceo/api/breed/{self.raca}/images')
            self.imgs = self.res.json()['message']
            self.arquivo = self.imgs[randint(0, len(self.imgs) - 1)]
            print(self.arquivo)
        else:
            self.raca = raca
            self.subraca = subraca
            self.res = requests.get(f'https://dog.ceo/api/breed/{self.raca}/images').json()['message']
            self.list = []
            for i in self.res:
                if f'{self.raca}-{self.subraca}' in i:
                    self.list.append(i)
            self.arquivo = self.list[randint(0, len(self.list) - 1)]
            print(self.arquivo)

    def enviar(self):
        try:
            message = MIMEText(f"""<img src='{self.arquivo}' width='400' height='400'><br> Essa linda imagem foi enviada utilizando Python.<br>
                                Esse é um {self.raca}""", 'html', 'utf-8')
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

email = DogsMail(username='Seu email', password='Sua senha')
email.requisicao(raca='Uma raça', subraca='Uma subraca, caso tenha.')
email.enviar()