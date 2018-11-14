import imaplib
import email
import time
import os
import re
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
IMAP_SERVER = os.environ.get('IMAP_SERVER')
PATH_TO_FIREBASE_CREDENTIALS = os.environ.get('PATH_TO_FIREBASE_CREDENTIALS')
DATABASE = os.environ.get('DATABASE')
POLLING_INTERVAL = int(os.environ.get('POLLING_INTERVAL'))


cred = credentials.Certificate(PATH_TO_FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred)
db = firestore.client()

def store_in_firestore(from_mail, mail):
  print('Storing new email')
  print(from_mail)
  print(mail)
  db.collection(DATABASE).document(from_mail).set(mail)

def check_new_mails():
  mail = imaplib.IMAP4_SSL(IMAP_SERVER)
  (retcode, capabilities) = mail.login(EMAIL, PASSWORD)
  mail.list()
  mail.select('inbox')
  (retcode, mails) = mail.search(None, '(UNSEEN)')
  if retcode == 'OK':
    for num in mails[0].split() :
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
        if isinstance(response_part, tuple):
          try:
            new_mail = email.message_from_string(response_part[1].decode('utf-8'))
            body = ''
            try:
              body = new_mail.get_payload(decode=True).decode('utf-8')
            except:
              body = new_mail.get_payload(0)
              while body.is_multipart():
                body = body.get_payload(0)
              body = body.get_payload(decode=True).decode('utf-8')
            store_in_firestore(
              new_mail['date'],
              {
                'customerEmail': re.sub(r'[<>]', '', new_mail['from']).split()[-1],
                'subject': new_mail['subject'],
                'body': body
              }
            )
            typ, data = mail.store(num,'+FLAGS','\\Seen')
          except:
            pass

if __name__ == '__main__':
  while True:
    try:
      check_new_mails()
    except:
      pass
    time.sleep(POLLING_INTERVAL)

