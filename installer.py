import platform
def install(plat):
    print("Vermillion RPC Bot installer")
    dir = str(input("Please input the full path where you wish the program to install to (the installer will make its own folder in this directory) "))
    try:
        pass
    except Exception as e:
        print("An exception has occurred during the install process")
        print(str(e))
        print("The program will now close.")
    pass
plat = platform.system()
install(plat)