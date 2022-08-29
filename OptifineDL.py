#Imports--------------------------
import linecache
from termcolor import colored
import requests
import time
from optipy import getUrl
import time
import os
import glob
import psutil
#--------------------------------

#Define important values---------
langpath = "languages/ENG-EN.txt"
dbug = 0
#--------------------------------

#Define title values------------------------------------------------------------------------------
title1 =r" _______  _______  _______  ___   _______  ___   __    _  _______  ______   ___       "
title2 =r"|       ||       ||       ||   | |       ||   | |  |  | ||       ||      | |   |      "
title3 =r"|   _   ||    _  ||_     _||   | |    ___||   | |   |_| ||    ___||  _    ||   |      "
title4 =r"|  | |  ||   |_| |  |   |  |   | |   |___ |   | |       ||   |___ | | |   ||   |      "
title5 =r"|  |_|  ||    ___|  |   |  |   | |    ___||   | |  _    ||    ___|| |_|   ||   |___   "
title6 =r"|       ||   |      |   |  |   | |   |    |   | | | |   ||   |___ |       ||       |  "
title7 =r"|_______||___|      |___|  |___| |___|    |___| |_|  |__||_______||______| |_______|  "

fulltitle=(title1+"\n" + title2+"\n"+title3 + "\n" + title4 + "\n" + title5 + "\n" + title6 + "\n" + title7 + "\n")

#-------------------------------------------------------------------------------------------------



os.system("cls") #Clear console



print (fulltitle) #Print title


#Language selector-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Select program language (default: English):")
print("[1] English")
print("[2] Italian/Italiano")
language = input('>> ')




    #Define language and langpath and print selected language
if language == "1":
    print("English selected.")
    langpath = "languages/ENG-EN.txt"
elif language == "2":
    print("Italiano selezionato.")
    langpath = "languages/ITA-IT.txt"
elif language == "":
    language = 1
    print("English selected.")
    langpath = "languages/ENG-EN.txt"
else:
    print("Invalid input, english selected.")
    langpath = "languages/ENG-EN.txt"

    #Define every message in the selected language
l1 = linecache.getline(langpath,1).rstrip('\n') # Warning! The program automatically identifies processes to automate some actions. Please close every "javaw" istance to avoid eventually errors.
l2 = linecache.getline(langpath,2).rstrip('\n') # Select the version...
l3 = linecache.getline(langpath,3).rstrip('\n') # Looking for the version in the database...
l4 = linecache.getline(langpath,4).rstrip('\n') # Version found!
l5 = linecache.getline(langpath,5).rstrip('\n') # Preparing the URL for the browser...
l6 = linecache.getline(langpath,6).rstrip('\n') # The URL is:
l7 = linecache.getline(langpath,7).rstrip('\n') # Downloading the file...
l8 = linecache.getline(langpath,8).rstrip('\n') # File downloaded!
l9 = linecache.getline(langpath,9).rstrip('\n') # Starting psutil...
l10 = linecache.getline(langpath,10).rstrip('\n') # psutil started!
l11 = linecache.getline(langpath,11).rstrip('\n') # Warning! A javaw istance has been found. Do you want to close it now? [Y] Yes [N] No (default: No):
l12 = linecache.getline(langpath,12).rstrip('\n') # Closing javaw...
l13 = linecache.getline(langpath,13).rstrip('\n') # javaw will not be closed.
l14 = linecache.getline(langpath,14).rstrip('\n') # Invalid input, javaw will not be closed.
l15 = linecache.getline(langpath,15).rstrip('\n') # Can't find javaw.
l16 = linecache.getline(langpath,16).rstrip('\n') # Optifine has been opened, proceed the installation on its window...
l17 = linecache.getline(langpath,17).rstrip('\n') # I can still see javaw.
l18 = linecache.getline(langpath,18).rstrip('\n') # Optifine has been closed.
l19 = linecache.getline(langpath,19).rstrip('\n') # Warning! Can't identify Optifine window, proceed the installation on its window and press any button after the installation is completed.
l20 = linecache.getline(langpath,20).rstrip('\n') # Deleting downloaded file...
l21 = linecache.getline(langpath,21).rstrip('\n') # File deleted succesfully!
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


os.system('cls') #Clear console
print(fulltitle) #Print title


#Select the version----------------------------------

#Write "debug" to enter debug mode and see debug outputs

print(colored(l1,'red'))
version = input(l2 + '\n' + '>> ')
if version == ("debug"):
    dbug = 1
    version = input(l2 +'\n' + 'Debug mode' + '\n' + '>> ')
    print(dbug)
#----------------------------------------------------




#Define important values to find Enviroments Paths removing backslashes and spaces
nospace = " "
userprofile = os.getenv('USERPROFILE') + r"\ " + "downloads\ "
if dbug == 1:
    print (userprofile)
userprofile = str(userprofile)
userprofile = userprofile.replace(" ","")
userprofile = userprofile.replace(os.sep,"/")
if dbug == 1:
    print (userprofile)
#---------------------------------------------------------------------------------


#Looking for version in database using optipy----------------------------
print (l3)

while True:
    data = getUrl(mcversion=str(version), single=True, timeout=15)
    if "408" not in data:
        if dbug == 1:
         print(data)

        break
#-----------------------------------------------------------------------

# Preparing URL for download---------
print(l4)
url = str(data).removesuffix("']")
url = str(url).removeprefix("['")
print(l5)
if dbug == 1:
    print (l6 + url)
#------------------------------------






#Looking for the path of the file---------------------------
file = url.removeprefix("https://optifine.net/download?f=")
path = str((userprofile + str(file)))
file = str(file)
path = str(path)
#-----------------------------------------------------------



# Download the file using response -------
print(l7)

response = requests.get(url)
open(path, "wb").write(response.content)

print(l8)
#-----------------------------------------


# Wait for the file to downlaod------
while True:
    if glob.glob(path):
        break
#------------------------------------


#Starts psutil to indentify processes-------------------------------------------------------
if dbug == 1:
    print(l9)

def checkProcessRunning(processName):
    # Checking if there is any running process that contains the given name processName.
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
if dbug == 1:
    print(l10)
#-------------------------------------------------------------------------------------------


#Checks if another Javaw istance is open to avoid conflicts-------
Automatico = 0
chiudere = ("y")
if checkProcessRunning('javaw.exe'):
        chiudere = input(colored(l11+"\n","red"))
        chiudere = chiudere.lower()
        if chiudere == ("y"):
            print (l12)
            os.system("taskkill /f /im javaw.exe")
        elif chiudere == ("n"):
            print (l13)
            Automatico = 1
        elif chiudere == (""):
            print (l13)
            Automatico = 1
        else:
            print(l14)
            Automatico = 1
#-----------------------------------------------------------------
    

time.sleep(1) #Sleep to avoid errors

os.startfile(path) # Starts downloaded file



# Check if jawaw is running --------------------------------------------------------------------



if chiudere ==("y"):
    while True:
        if dbug == 1:
            print(l15)
        if checkProcessRunning('javaw.exe'):
            print(l16)
            while True:
                if dbug == 1:
                    print(l17)
                if not checkProcessRunning('javaw.exe'):
                
                    print(l18)
                    break
            break
else:
    if Automatico == 1:
        print(colored(l19,"red"))
        
    
#---------------------------------------------------------------------------------------------


os.system('pause') #Pause before file will be deleted

#Delete file----
print(l20)
time.sleep(3)
os.remove(path)
print(l21)
#---------------

#Debug values ------------------------------------------------
if dbug == 1:
    print("Debug values")
    print (data)
    print (url)
    print (file)
    print (path)
#-------------------------------------------------------------


os.system('pause') #Final pause to read debug values if in debug mode
