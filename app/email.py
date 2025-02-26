from app import app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(subject, sender, recipients, text_body, html_body=None):
    message = Mail(
        from_email=sender,
        to_emails=recipients,
        subject=subject,
        plain_text_content=text_body,
        html_content=html_body if html_body else text_body
    )
    try:
        sg = SendGridAPIClient(app.config['MAIL_PASSWORD'])
        response = sg.send(message)
        print(f'Email enviado correctamente, {response.status_code}')
    except Exception as e:
        print(f'Error enviando email: {e}')