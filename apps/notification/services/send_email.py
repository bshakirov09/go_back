from goplaciz.settings import SENDGRID_API_KEY, SEND_GRID_FROM_EMAIL
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)


def send_email_with_send_grid(email: str, subject: str, html_content: str):
    message = Mail(
        from_email=SEND_GRID_FROM_EMAIL,
        to_emails=email,
        subject=subject,
        plain_text_content=html_content
    )
    sg.send(message)