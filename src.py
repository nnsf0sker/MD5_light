import hashlib
import requests
import smtplib
import os
import sys

OUTGOING_EMAIL = "test@gmail.com"
OUTGOING_EMAIL_PASS = "1234"
OUTGOING_EMAIL_SMTP = "smtp.gmail.com"
OUTGOING_EMAIL_SMTP_PORT = 587

def md5(url):
    hash_md5 = hashlib.md5()
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=2**20):
            if chunk:
                hash_md5.update(chunk)
    return hash_md5.hexdigest()

def send_email(destination_email, message):
    smtpObj = smtplib.SMTP(OUTGOING_EMAIL, OUTGOING_EMAIL_SMTP_PORT)
    smtpObj.starttls()
    smtpObj.login(OUTGOING_EMAIL, OUTGOING_EMAIL_PASS)
    smtpObj.sendmail(OUTGOING_EMAIL, destination_email, str(message))
    smtpObj.quit()

def printToTheFile(id, status):
    f = open(os.path.join("buff", id + ".txt"), 'wt')
    if status == "done":
        f.write(status+"\n")
        f.write(url+"\n")
        f.write(md5+"\n")
    elif status == "running":
        f.write(status+"\n")
    elif status == "fail":
        f.write(status+"\n")
    f.close()

id = sys.argv[1]
printToTheFile(id=id, status="running")

if len(sys.argv) == 3:
    try:
        url = sys.argv[2]
        hashSum = md5(url)
        printToTheFile(id=id, status="done", url=url, md5=hashSum)
    except:
        printToTheFile(id=id, status="fail")
        sys.exit()

elif len(sys.argv) == 4:
    try:
        url = sys.argv[2]
        hashSum = md5(url)
        destination_email = sys.argv[3]
        # send_email(destination_email, hashSum)
        printToTheFile(id=id, status="done")
    except:
        printToTheFile(id=id, status="fail")
        sys.exit()