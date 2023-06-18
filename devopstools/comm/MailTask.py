#!/usr/bin/python

import smtplib
import ssl

import os
from pathlib import Path

import jsonschema
from jsonschema import validate
import json


class MailTask(object):

    def getMailConfig(self, exampleName):
        parent = Path(__file__).parent.parent
        configDir = (parent / 'config').resolve()
        print(configDir)

        for schema in configDir.glob("*.json"):
            jsonfile = schema.name
            fn = jsonfile[:-5]
            if fn == exampleName:
                js = Path(configDir / jsonfile).read_text()
                return json.loads(js)

    def sendMail(self, message):
        js = self.getMailConfig("mail")
        port = js.get('port')
        smtp_server = js.get('smtp_server')
        sender = js.get('sender')
        recipient = js.get('recipient')
        password = js.get('password')
        payload_file = js.get('payload_file')

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                # server.ehlo()  # Can be omitted
                server.starttls()
                # server.ehlo()  # Can be omitted
                server.login(sender, password)
                print('Successfully Connected to server')
                server.sendmail(sender, recipient, message)
                server.quit()
        except smtplib.SMTPException:
            print("Error: unable to send email")


if __name__ == "__main__":
    message = """From: Srikari Rallabandi <srikari.rallabandi@inveniolsi.com>
    To: DevOPS-Dashboard <DevOPS_Dashboard@inveniolsi.com>
    Subject: Alert e-mail test

    This is a test e-mail message from the refactored code.
    """
    mt = MailTask()
    mt.sendMail(message)
