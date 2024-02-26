Live Video Capture and Monitoring with Streamlink
Overview
This Python project allows you to monitor live video streams from specific URLs using the Streamlink library. It logs the stream captures and provides email notifications in case of any issues.

Requirements
Python 3.x
Streamlink library
SMTP server for sending email notifications
Installation
Install Python 3.x from python.org.
Install Streamlink using pip:
pip install streamlink
Set up your SMTP server for sending email notifications.
Usage
Clone this repository to your local machine.
Modify the configuration file e-posta.py to specify the URL to capture, email settings, and any other parameters.
Run the main script:
python youtube_control.py
The script will start capturing the live video stream, logging the captures, and sending email notifications based on the configured conditions.
Configuration
You can customize the behavior of the script by modifying the parameters in the config.py file. Here are some key configurations:

STREAM_URL: The URL of the live video stream to capture.
LOG_FILE: Path to the log file where capture records will be stored.
SMTP_SERVER: SMTP server address for sending email notifications.
EMAIL_FROM: Sender email address.
EMAIL_TO: Recipient email address(es).
EMAIL_SUBJECT: Subject line for email notifications.
EMAIL_BODY: Body text for email notifications.
License
This project is licensed under the MIT License.

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


Türkçe Açıklama:
Bu uygulama Python üzerinde streamlink kullanarak canlı yayın kontrolü yapmaktadır. Asenkron metot kullanılarak birden fazla url'den yayın kontrolü sağlanmaktadır. Bu programın amacı canlı yayının mevcut olup olmadığını öğrenmek ve bunun üzerinde bilgilendirme yapmaktır. Aynı zamanda log dosyası tutarak geçmişe yönelik bilgileride elinizde bulundurabileceksiniz. Bilgilendirme için e-posta.py kullanılmaktadır. e-posta.py de sizler için paylaşılmış, gereken bilgileri doldurduğunuz taktirde hata durumunda mesaj alabileceksiniz.+
