#!/usr/bin/env python3

from GModServer import Variables
import os

def StartGarrysModServer(steanApiAuthKey=Variables.SteamApiAuthKey, steamWorkShopID=Variables.SteamWorkShopId,
                         serverGamemode=Variables.ServerGamemode, serverDefaultMap=Variables.ServerDefaultMap,
                         serverPort=Variables.ServerPort, serverMaxPlayer=Variables.ServerMaxPlayer,
                         serverRunFile=Variables.ServerRunFile, debug=False):

    Command="%s -game garrysmod +maxplayers %s -authkey %s +host_workshop_collection %s +map %s +gamemode %s +port " \
            "%s" % (serverRunFile, serverMaxPlayer, steanApiAuthKey,
                    steamWorkShopID, serverDefaultMap, serverGamemode, serverPort)
    if(debug==True):
        print(Command)
    os.system(Command)                          #start gMod server



if __name__ == '__main__':
    from PythonServerKernel.Exceptions import RunnedFromFalseFile
    raise RunnedFromFalseFile('GModServer_StartServer_py')