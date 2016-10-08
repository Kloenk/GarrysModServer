#!/usr/bin/env python3

from GModServer.Variables import *

def sendStartEMail(steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer, serverPort):
    from eMail.StartTextFile import SendStartEMail
    SendStartEMail(steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer, serverPort)

def StartServer(steamApiAuthKey=SteamApiAuthKey, steamWorkShopId=SteamWorkShopId, serverGamemode=ServerGamemode, serverDefaultMap=ServerDefaultMap, serverMaxPlayer=ServerMaxPlayer, serverPort=ServerPort):
    print("start")
    sendStartEMail(steamWorkShopId, serverGamemode, serverDefaultMap, serverMaxPlayer, serverPort)



if __name__ == '__main__':
    from PythonServerKernel.Exceptions import RunnedFromFalseFile
    raise RunnedFromFalseFile('startServer_py')
