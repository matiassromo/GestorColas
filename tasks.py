from celery_app import app
import smtplib
from email.mime.text import MIMEText

@app.task
def send_email(subject, body, to_email):
    from_email = "matiasromo10@hotmail.com"
    password = "california2003"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP_SSL('smtp.example.com', 465)
        server.login(from_email, password)
        server.sendmail(from_email, [to_email], msg.as_string())
        server.quit()
        return "Email sent successfully"
    except Exception as e:
        return str(e)
