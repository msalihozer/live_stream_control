from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Eposta():
    try:
        # E-posta bilgileri
        myMailAdress = "you_mail_adress"
        password = "Password!"
        sendTo = ["xxx@xxx.com"]  # Alıcı e-posta adresleri
        subject = "Title"
        message = "Message"

        # E-posta oluşturma
        msg = MIMEMultipart()
        msg['From'] = myMailAdress
        msg['To'] = ", ".join(sendTo)
        msg['Subject'] = subject

        # E-posta içeriğini eklemek
        msg.attach(MIMEText(message, 'plain'))

        # SMTP sunucusuna bağlanma
        mail = SMTP("smtp.office365.com", 587)
        mail.starttls()  # TLS şifrelemesi başlat
        mail.login(myMailAdress, password)

        # E-posta gönderme
        mail.sendmail(myMailAdress, sendTo, msg.as_string())
        print("E-posta başarıyla gönderildi.")

        # Bağlantıyı kapat
        mail.quit()
    except Exception as e:
        print("Hata Oluştu!\n {0}".format(e))




