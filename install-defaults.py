import subprocess
import time
# pre install setup mainly for steam
subprocess.run("sudo add-apt-repository multiverse", shell=True)
subprocess.run("sudo dpkg --add-architecture i386", shell=True)
subprocess.run("sudo apt update", shell=True)
subprocess.run("sudo apt upgrade -y", shell=True)
# install the applications
# IF YOU WANT TO MODIFY WHAT IS INSTALLED, JUST TYPE IN THE PACKAGE BELOW, OR REMOVE ANY YOU DO NOT WANT
# subprocess.run("sudo snap install xyz -y", shell=True) # INSTALLS ANY SNAP PACKAGES IF YOU WISH TO ADD THOSE. REMEMBER TO UPDATE SNAP REPOS AS WELL 
subprocess.run("sudo apt install audacity gnome-shell-extension-manager steam gnome-software gnome-tweaks flatpak gnome-software-plugin-flatpak vlc gimp -y", shell=True)
# setup flatpak
subprocess.run("sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flathub.repo", shell=True)

# ask the user (me) if they have rebooted yet? this is a key step after adding flatpak.
hasrebooted = input("Have you rebooted yet? This is required for flatpak to properly setup, and for the system to not be broken (y/N)")
if hasrebooted == "n" or hasrebooted == "N":
    print("Restarting in 10 seconds. Please restart script after reboot to continue with flatpak app setup")
    time.sleep(10)
    
    # reboots
    subprocess.run("sudo reboot", shell=True)
if hasrebooted == "y" or hasrebooted == "Y": # assuming they say yes and are being truthful.
    print("Continuing the Installation. Please do Control + C in the next 10 seconds if you have not restarted. this is a last warning")
    time.sleep(10)
    
    # not sure why i added it down here. but i did. last apt install
    subprocess.run("sudo apt install gnome-software-plugin-flatpak -y", shell=True)
    
    # from now its all flatpak
    # IF YOU WANT TO MODIFY THE DEFAULT FLATPAK APPS, REMOVE OR ADD LINES TO ADD YOUR DESIRED APPLICATIONS. YOU CAN FIND INFO ON WHAT THE PACKAGE NAMES ARE ON THE FLATHUB WEBSITE
    subprocess.run("flatpak install flathub com.vscodium.codium -y", shell=True)
    subprocess.run("flatpak install flathub com.protonvpn.www -y", shell=True)
    subprocess.run("flatpak install flathub io.lmms.LMMS -y", shell=True)
    subprocess.run("flatpak install flathub org.musescore.MuseScore -y", shell=True)
    subprocess.run("flatpak install flathub org.prismlauncher.PrismLauncher -y", shell=True)

    print("All Apps have installed. Please check back for any errors and resolve them if possible. Will quit now")
    time.sleep(5)
