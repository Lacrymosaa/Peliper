import smtplib
from mail_service import get_mails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(destinatario, assunto, mensagem, remetente, senha):
    # Configuração do servidor SMTP
    servidor_smtp = 'smtp.gmail.com'
    porta_smtp = 587

    # Criando o objeto do email
    email = MIMEMultipart()
    email['From'] = remetente
    email['To'] = destinatario
    email['Subject'] = assunto

    # Anexando o texto do email
    corpo_email = MIMEText(mensagem, 'plain')
    email.attach(corpo_email)

    # Conectando ao servidor SMTP e enviando o email
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, email.as_string())
    servidor.quit()

# Informações do email
assunto = f'teste' # Assunto
mensagem = f"""
Olá,

Espero que tenha um bom-dia!
    
Atenciosamente,
Peliper!
""" # Mensagem que irá junto no e-mail
remetente = '@gmail.com' # Seu e-mail
senha = '' # A senha obtida no Senhas do app do Google

emails_array = get_mails()

# Enviar o email
for destinatario in emails_array:
    enviar_email(destinatario, assunto, mensagem, remetente, senha)
print("Enviado com sucesso!")
