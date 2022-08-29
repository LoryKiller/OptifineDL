import os
os.system("FOR /F %k in (requirements.txt) DO ( if NOT # == %k ( pip install %k ) )")
os.system("python optifine2.py")