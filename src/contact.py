import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Environmental Variables
SENDING_EMAIL = os.environ.get("SENDING_EMAIL")
RECEIVING_EMAIL = os.environ.get("RECEIVING_EMAIL")
SENDING_PASSWORD = os.environ.get("SENDING_PASSWORD")


class NotificationManager:
    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message

    def compose_email(self):
        email_body = f"""
		<h3>New Contact Form Submission</h3>
		<p><strong>From: </strong>{self.name}</p>
		<p><strong>Email: </strong>{self.email}</p>
		<p><strong>Phone: </strong>{self.phone}</p>
		<p><strong>Message: </strong>{self.message}</p>
		"""
        return email_body

    def send_email(self):
        message = EmailMessage()
        message["From"] = SENDING_EMAIL
        message["To"] = RECEIVING_EMAIL
        message["Subject"] = "New Website Contact Form Submission"
        message.set_content(self.compose_email(), subtype="html")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDING_EMAIL, password=SENDING_PASSWORD)
            connection.sendmail(
                from_addr=SENDING_EMAIL,
                to_addrs=RECEIVING_EMAIL,
                msg=message.as_string(),
            )
