# Install My Defaults
This is a small script i wrote for myself to install my preferred default apps on Ubuntu Linux.
If you want to install my default apps on your device, make sure you have:
- Ubuntu Linux (Tested on 26.04, likely will work on most versions with active repositories)
- Python
- An internet connection

To run it, simply download the python file, open terminal, and run `python3 install-defaults.py`, It will automatically install the apt packages, prompt you for a restart (type y if you have already restarted, otherwise type n to restart then), and rerun the file on system restart to install the flatpak apps. Make sure to say 'y' after you restart it so that it doesn't restart unneccesarily
