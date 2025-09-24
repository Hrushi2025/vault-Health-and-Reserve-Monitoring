# deploy/alerts.py

def send_slack(message: str):
    """
    Placeholder function to send a Slack message.
    Replace this with actual Slack API integration.
    """
    print(f"[Slack Alert] {message}")


def send_email(subject: str, body: str, to: str):
    """
    Placeholder function to send an email.
    Replace this with actual SMTP / email service integration.
    """
    print(f"[Email to {to}] Subject: {subject}\nBody: {body}")
