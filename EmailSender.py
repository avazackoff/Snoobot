import sys
from email.header import Header
import AppConfig as cfg
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content, Cc, Attachment, FileContent, FileName, FileType, Disposition, ContentId

class EmailSender:
    def __init__(self, logger):
        logger.info("Creating Email Class")
        self.sg = SendGridAPIClient(api_key=cfg.Email["SendgridApiKey"])
        self.logger = logger

    def sendEmail(self, emailTo, emailSubject, emailBody):
        self.logger.info("Constructing email message")
        from_email = Email(str(Header(cfg.Email["From"])))
        to_email = To(emailTo)
        subject = emailSubject
        content = Content("text/plain", emailBody)
        mail = Mail(from_email, to_email, subject, content)
        mail_json = mail.get()
        try:
            self.logger.info("Sending email message")
            response = self.sg.client.mail.send.post(request_body=mail_json)
            self.logger.info("Email Sent. Response Status Code: {0}".format(str(response.status_code)))
        except:
            self.logger.error(sys.exc_info())
            raise
