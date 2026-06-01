import smtplib
from email.message import EmailMessage
EMAIL = "piyushcode499@gmail.com"
APP_PASSWORD = "hhvwujesptcsepum"

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = "piyushmaurya222007@gmail.com"
msg["Subject"] = "CSV Data File"

with open("Piyush.csv", "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="text",
        subtype="csv",
        filename="Piyush.csv"
    )
    
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)
                        
print("Now say him to see mail")

