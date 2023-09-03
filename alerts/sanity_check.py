from dotenv import load_dotenv
import os,  datetime, pytz, smtplib
from email.message import EmailMessage

load_dotenv()
EMAIL_PASS = os.environ['EMAIL_PASS']
SENDER = os.environ['SERVER_EMAIL']
RECIPIENTS = os.environ['SANITY_CHECK_EMAIL_RECIPIENTS']

class Email:
    def __init__(self):
        self.recipients = RECIPIENTS
        self.password = EMAIL_PASS 
        self.sender = SENDER
        self.datetime = datetime.datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%m/%d/%Y, %H:%M:%S")

    def sanity_check_alert(self):
        try:
            msg = EmailMessage()
            msg["Subject"] = "WhatsApp Chatbot - Sanity Check Alert"
            msg["From"] = self.sender
            msg["To"] = self.recipients

            body = f"""

  Hi Hasnain,

  Docker image has been tested and pushed to the remote repo at {self.datetime} VN local time.
  awaiting sanity checks befor going for deployment...

  Note: Do not reply to this email as this is a system-generated alert.
  
  Regards,
  AIOps
            """
            msg.set_content(body)

            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(self.sender, self.password)
                print("log in successfull!! \nsending email")
                smtp.send_message(msg)
                # print(f"email Sent to {self.recipients}")

        except Exception as e:
            raise e