import smtplib
import getpass
from security_info import passwords,emails

def send_email_confirm_registration(username,password, code, to_email):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = emails["outlook"]

    MESSAGE = f"""Subject: Send email from Nhom13

    Hello {username} are you register new acc .

    Here are your code :

    {code}

    Remember your code is only valid for 3 minutes
    """

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, password)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, to_email, MESSAGE)
    smtp.quit()

    print("Email sent successfully")
    return "Email sent successfully"