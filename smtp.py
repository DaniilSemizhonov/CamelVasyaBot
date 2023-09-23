import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = "" # @gmail.com
    password = "" # password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "CamelVasyaBot"
        server.sendmail(sender, "admin email adress", msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"
