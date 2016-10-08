#!/usr/bin/env python3

#TODO Kommentare einfügen

if __name__ == '__main__':
    print("programm running")
    print("sending start email")
    import GModServer.startServer
    GModServer.startServer.StartServer()
    import GModServer.UpdateAndValidateServer
    GModServer.UpdateAndValidateServer.updateGarrysModServer()
