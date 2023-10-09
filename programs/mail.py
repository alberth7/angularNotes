import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set your Gmail credentials
sender_email = "maikeru.bash@gmail.com"
sender_password = ""

# Create the SMTP connection
smtp_server = "smtp.gmail.com"
smtp_port = 587
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
except Exception as e:
    print(f"Failed to connect to the SMTP server: {e}")
    exit()

# Compose and send 50 messages
for i in range(2):
    receiver_email = "apazaalberth7@gmail.com"  # Replace with the recipient's email address
    subject = f"Subject of Message {i + 1}"
    message_body = f"Hello, this is Message {i + 1} sent from Python."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message_body, "plain"))

    try:
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Message {i + 1} sent successfully.")
    except Exception as e:
        print(f"Failed to send Message {i + 1}: {e}")

# Close the SMTP connection
server.quit()
