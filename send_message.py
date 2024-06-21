from tasks import send_email

if __name__ == "__main__":
    send_email.delay("Test Subject", "Hello World!", "matiasromo03@gmail.com")
