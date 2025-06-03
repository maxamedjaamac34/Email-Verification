import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

def send_verification_email(to_email: str, token: str):
    link = f"http://localhost:8000/verify-email?token={token}"
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject="Verify Your Email",
        html_content=f"Click <a href='{link}'>here</a> to verify your email."
    )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)
