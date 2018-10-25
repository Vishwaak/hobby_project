from apiclient.discovery import build
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode


SENDER = "xerous07@gmail.com"
RECIPIENT = "xerous07@gmail.com"
SUBJECT = "mine"
CONTENT = "Hero is great u idiot" 
SCOPE = 'https://www.googleapis.com/auth/gmail.compose' 

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('cer.json', SCOPE)
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))



def create_message(sender, to, subject, message_text):
 
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  encoded_message = urlsafe_b64encode(message.as_bytes())
  return {'raw': encoded_message.decode()}



def send_message(service, user_id, message):
  
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message
  #except errors.HttpError, error:
  except(errors.HttpError):
    print('ERROR LOG' , errors.HttpError)


raw_msg = create_message(SENDER, RECIPIENT, SUBJECT, CONTENT)
print(raw_msg)
send_message(service, 'xerous07@gmail.com', raw_msg)
