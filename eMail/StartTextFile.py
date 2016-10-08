#!/usr/bin/env python3

import smtplib

import sys
from email.mime.text import MIMEText

def SendStartEMail(steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer, serverPort):
    text = '''
    The GCG Server Will now start.
    The steamWorkshopId from the pack is %s, the Gamode of the server is %s, the map is %s, there are %s players allowed, the server is runing on port %s.
    ''' % (steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer, serverPort)
    msg = MIMEText(text, 'plain')
    msg['Subject'] = "starting info"
    msg['to']      = '[GCG] Root Server Managment'
    msg['From']    = '[GCG] Root Server'
    try:
        conn = smtplib.SMTP_SSL('mail.gmx.net:465')
        conn.set_debuglevel(True)
        conn.login('kloenk@gmx.de', 'R3ich3lt')		#TODO andere eMail einstellen
        try:
            conn.sendmail('kloenk@gmx.de', 'speechinterface15@gmail.com; finn@trudeltiere.de', msg.as_string())
        finally:
            conn.close()
    except Exception as exc:
        print("critical Error")



if __name__ == '__main__':
    from GModServer.Variables import *
    SendStartEMail(SteamWorkShopId, ServerGamemode, ServerDefaultMap, ServerMaxPlayer, ServerPort)
