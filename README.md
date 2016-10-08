# GarrysModserver
A Python 3 script to run a grays Mod Server with email info created for:

![GitHub Logo](http://germancommunitygaming.de/styles/WoWDraenor/theme/images/logo.png)




#Use This Programm
To use this programm you must have:
-installed SteamCmd
-creat the file Variables.py und GModServer with the folowing thing:


    #!/usr/bin/env python3

    SteamApiAuthKey = ""                #your Steam Api Auth Key
    SteamWorkShopId =                   #the Id Of the workshop collection you will use
    ServerGamemode  = ""                #the gamode you will run
    ServerDefaultMap= ""                #the Standart map of your server
    ServerPort      =                   #the port from your channel
    ServerMaxPlayer =                   #the max users of your server
    ServerRunFile   = ""                #the file that will run your gMod Server
    SteamAuthName   = ""                #your steam Name for login into steamcmd
    SteamForceDir   = ""                #the director in that you wil install yout GMod
    SteamApID       = 4020              #the app Id of GMod Server
    SteamCmdDir     = ""                #your steamcmd file path
    ServerEmailAddr = ""                #the eMail Address from that the server should send infos
    ServerEmailPwd  = ""                #the password to the email above
    AdminEmailAddres= ""                #the email who should become the infos
    SMTPServerAddres=''                 #the Url from your SMTP server (domain:port (standart port 25))



    if __name__ == '__main__':
        from PythonServerKernel.Exceptions import RunnedFromFalseFile
        raise RunnedFromFalseFile('GModServer_Variables_py')
