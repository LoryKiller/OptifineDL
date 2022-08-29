import os
os.system("FOR /F %k in (requirements.txt) DO ( if NOT # == %k ( pip install %k ) )")

title1 =r" _______  _______  _______  ___   _______  ___   __    _  _______  ______   ___       "
title2 =r"|       ||       ||       ||   | |       ||   | |  |  | ||       ||      | |   |      "
title3 =r"|   _   ||    _  ||_     _||   | |    ___||   | |   |_| ||    ___||  _    ||   |      "
title4 =r"|  | |  ||   |_| |  |   |  |   | |   |___ |   | |       ||   |___ | | |   ||   |      "
title5 =r"|  |_|  ||    ___|  |   |  |   | |    ___||   | |  _    ||    ___|| |_|   ||   |___   "
title6 =r"|       ||   |      |   |  |   | |   |    |   | | | |   ||   |___ |       ||       |  "
title7 =r"|_______||___|      |___|  |___| |___|    |___| |_|  |__||_______||______| |_______|  "

fulltitle=(title1+"\n" + title2+"\n"+title3 + "\n" + title4 + "\n" + title5 + "\n" + title6 + "\n" + title7 + "\n")

print (fulltitle) 

print('Requirements succesfully installed. Open the start.bat file to run the program')