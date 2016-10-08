#!/usr/bin/env python3

from GModServer.Variables import *

def sendStartEMail(steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer,serverIp, serverPort):
    from eMail.StartTextFile import SendStartEMail
    SendStartEMail(steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer,serverIP=serverIp, serverPort=serverPort)

def StartServer(steamApiAuthKey=SteamApiAuthKey, steamWorkShopId=SteamWorkShopId, serverGamemode=ServerGamemode,
                serverDefaultMap=ServerDefaultMap, serverMaxPlayer=ServerMaxPlayer,serverIp=ServerIp, serverPort=ServerPort, debug=False):
    print("start")
    sendStartEMail(steamWorkShopId, serverGamemode, serverDefaultMap, serverMaxPlayer,serverIp, serverPort)
    from GModServer.UpdateAndValidateServer import updateGarrysModServer
    updateGarrysModServer(debug=debug)                                      #update gMod Server over steamcmd
    from GModServer.StartServer import StartGarrysModServer
    StartGarrysModServer(debug=debug)                                       #Start GMod Server



if __name__ == '__main__':
    from PythonServerKernel.Exceptions import RunnedFromFalseFile
    raise RunnedFromFalseFile('GModServer_SendStartMail_py')
