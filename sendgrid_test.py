import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# ✅ Load .env from current directory
load_dotenv(dotenv_path=".env")

# ✅ Debug print to confirm it's working
print("Loaded API Key:", os.environ.get("SENDGRID_API_KEY"))

message = Mail(
    from_email='mohamedahmed@bennington.edu',
    to_emails='sdaauud@wesleyan.edu',
    subject='SendGrid Working Now!',
    html_content='Fuck you'
)

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(f"Status Code: {response.status_code}")
    print(f"Body: {response.body}")
    print(f"Headers: {response.headers}")
except Exception as e:
    print(e)
