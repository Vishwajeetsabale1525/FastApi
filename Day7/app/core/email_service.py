# app/core/email_service.py
def send_email(to_email: str, subject: str, body: str):
    # Mock function: In production, integrate with SMTP or external service
    print(f"Sending email to {to_email}:\nSubject: {subject}\nBody: {body}")
