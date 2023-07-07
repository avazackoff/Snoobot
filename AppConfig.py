import os
from dotenv import load_dotenv#remove
load_dotenv()#remove

SnooMetadata = {
    "Username": os.environ.get("SnooMetadata_Username"),
    "Password": os.environ.get("SnooMetadata_Password"),
    "LogFilePath": os.environ.get("SnooMetadata_LogFilePath"),
    "ConfigFilePath": os.environ.get("SnooMetadata_ConfigFilePath")
}

Email = {
    "SendgridApiKey": os.environ.get("Sendgrid_APIKey"),
    "From": os.environ.get("Email_From"),
    "To": os.environ.get("Email_To"),
}

googleCredentials = {
  "type": "service_account",
  "project_id": os.environ.get("googleProjectId"),
  "private_key_id": os.environ.get("googlePrivateKeyId"),
  "private_key": os.environ.get("googlePrivateKey"),
  "client_email": os.environ.get("googleClientEmail"),
  "client_id": os.environ.get("googleClientId"),
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ.get("client_x509_cert_url")
}

gSheetDetails = {
    "FileName": os.environ.get("googleFileName"),
    "SessionSheetName": os.environ.get("googleSessionSheetName"),
    "DaySheetName": os.environ.get("googleDaySheetName")
}