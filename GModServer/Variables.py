#!/usr/bin/env python3

SteamApiAuthKey = "1538A08B9734554D46E5FA6AED2DEB28"
SteamWorkShopId = 753026463
ServerGamemode  = "starwarsrp"
ServerDefaultMap= "rp_venator_rg"
ServerPort      = 27015
ServerIp        = '89.163.225.149'
ServerMaxPlayer = 50
ServerRunFile   = "/home/steam/steamcmd/garrysMod/srcds_run"
SteamAuthName   = "anonymous"
SteamForceDir   = "./garrysMod"
SteamApID       = 4020
#SteamCmdDir     = "/home/steam/steamcmd/steamcmd.sh"
SteamCmdDir     = "/home/finn/steamCWD/steamcmd.sh"
ServerEmailAddr = "kloenk@gmx.de"
ServerEmailPwd  = "R3ich3lt"
AdminEmailAddres= "speechinterface15@gmail.com"
SMTPServerAddres='mail.gmx.net:465'
#TODO weitere Variablen einfügen



if __name__ == '__main__':
    from PythonServerKernel.Exceptions import RunnedFromFalseFile
    raise RunnedFromFalseFile('GModServer_Variables_py')