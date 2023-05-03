import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Usando Biblioteca Template para trazer o texto em arquivo HTML e mandar texto por email.
html = Template(Path('index.html').read_text())
# Usando a função email para definir para quem vai o email.
email = EmailMessage()
email['from'] = 'kaian'
email['to'] = 'kaianc.personal@gmail.com'
email['subject'] = 'first email'
nome = 'kaian'
# Enviando email contendo uma variavel (nome) para poder mandar para mais de uma pessoa se precisar
# e personalizar para cada uma.
email.set_content(html.substitute({'name': 'Kaian'}), 'html')

# Podemos também definir uma mensagem única e mandar da seguinte forma:
# mensagem = 'Primeiro email automatizado!!!'
# email.set_content('{} {}'.format(nome, mensagem))

# função que vai logar no email que será usado para enviar o email ao destinatário.
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email que será usado para enviar os emails", "senha do email")
    smtp.send_message(email)
    # Imprimindo uma mensagem para avisar o que o código mandou o email.
    print('tudo certo chefe!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
