import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(destinatario, assunto, mensagem, arquivo_video, remetente, senha):
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

    # Anexando o vídeo
    anexo = open(arquivo_video, 'rb')
    parte_anexo = MIMEBase('application', 'octet-stream')
    parte_anexo.set_payload((anexo).read())
    encoders.encode_base64(parte_anexo)
    parte_anexo.add_header('Content-Disposition', "attachment; filename= %s" % arquivo_video)
    email.attach(parte_anexo)

    # Conectando ao servidor SMTP e enviando o email
    servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
    servidor.starttls()
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatario, email.as_string())
    servidor.quit()

# Lista de vídeos para cada dia da semana (segunda a domingo)
videos_por_dia = {
    'monday': 'weekday\\monday.mp4',
    'tuesday': 'weekday\\tuesday.mp4',
    'wednesday': 'weekday\\wednesday.mp4',
    'thursday': 'weekday\\thursday.mp4',
    'friday': 'weekday\\friday.mp4',
    'saturday': 'weekday\\saturday.mp4',
    'sunday': 'weekday\\sunday.mp4'
}

# Obter o dia da semana atual
dia_semana_atual = datetime.datetime.now().strftime('%A').lower()
video_atual = videos_por_dia[dia_semana_atual]

# Informações do email
destinatario = '@gmail.com' # Destinatario
assunto = f'Good {dia_semana_atual}' # Assunto
mensagem = f"""
Olá,

Espero que tenha um bom-dia! Aqui está seu vídeo do dia!
    
Atenciosamente,
Peliper!
""" # Mensagem que irá junto no e-mail
arquivo_video = video_atual  # Substitua pelo caminho do vídeo que deseja enviar
remetente = '@gmail.com' # Seu e-mail
senha = '' # A senha obtida no Senhas do app do Google

# Enviar o email
enviar_email(destinatario, assunto, mensagem, arquivo_video, remetente, senha)
print("Enviado com sucesso!")
