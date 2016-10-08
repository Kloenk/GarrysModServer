#!/usr/bin/env python3

import smtplib

import sys
from email.mime.text import MIMEText
from GModServer import Variables

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
        conn = smtplib.SMTP_SSL(Variables.SMTPServerAddres)
        conn.set_debuglevel(True)
        conn.login(Variables.ServerEmailAddr, Variables.ServerEmailPwd)		#TODO andere eMail einstellen
        try:
            conn.sendmail(Variables.ServerEmailAddr, Variables.AdminEmailAddres, msg.as_string())
        finally:
            conn.close()
    except Exception as exc:
        print("critical Error")



if __name__ == '__main__':
    #disables becaus it was to debug
    #from GModServer.Variables import *
    #SendStartEMail(SteamWorkShopId, ServerGamemode, ServerDefaultMap, ServerMaxPlayer, ServerPort)
    from PythonServerKernel.Exceptions import RunnedFromFalseFile
    raise RunnedFromFalseFile('eMail_StartTextFile_py')