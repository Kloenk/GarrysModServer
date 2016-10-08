#!/usr/bin/env python3

#import _thread

from GModServer import Variables
from PythonServerKernel.Exceptions import KernerlCriticalFailur
import os


def updateGarrysModServer(steamAuthName=Variables.SteamAuthName, steamAuthPwd="", steamForceDir=Variables.SteamForceDir,
                          steamAppID=Variables.SteamApID, validate=True, steamCmdDir=Variables.SteamCmdDir, debug=False):
    try:
        if(steamAuthPwd == ""):
            if(validate == True):

                Command="%s +login %s +force_install_dir %s +app_update %s validate " % (
                    steamCmdDir, steamAuthName, steamForceDir, steamAppID)

            elif(validate == False):
                Command = "%s +login %s +force_install_dir %s +app_update %s +quit" % (
                    steamCmdDir, steamAuthName, steamForceDir, steamAppID)
        elif(steamAuthPwd != ""):
            if(validate == True):
                Command = "%s +login %s %s +force_install_dir %s +app_update %s validate +quit" % (
                    steamCmdDir, steamAuthName,steamAuthPwd, steamForceDir, steamAppID)
            elif(validate == False):
                Command = "%s +login %s %s +force_install_dir %s +app_update %s +quit" % (
                    steamCmdDir, steamAuthName, steamAuthPwd, steamForceDir, steamAppID)
        else:
            raise KernerlCriticalFailur('SteamAuthPWD', '''can't resolve status''')
        if(debug== True):
            print("run command %s" % (Command))
        os.system(Command)
    except:
        raise


if __name__ == '__main__':
    from PythonServerKernel.Exceptions import  RunnedFromFalseFile
    raise RunnedFromFalseFile("GModServer_UpdateAndValidateServer_py")