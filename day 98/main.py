import smtplib
from email.message import EmailMessage
from datetime import datetime

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "vedanthtest4@gmail.com"
EMAIL_TO = "vedanthtest4@gmail.com"
APP_PASSWORD = "jahckmccnophtcef"


def send_raise_email():
    msg = EmailMessage()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = "Compensation Review Request"
    msg.set_content(
        "Hi [Name],\n\n"
        "I’d like to request a brief discussion to review my compensation "
        "in light of my recent contributions and impact. "
        "Happy to share specifics and align on next steps.\n\n"
        "Best regards,\n"
        "Vedanth"
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_FROM, APP_PASSWORD)
        server.send_message(msg)

    print(f"Sent at {datetime.now().isoformat()}")


if __name__ == "__main__":
    send_raise_email()
