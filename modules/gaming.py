from .service_module import run, install_packages

import os
import subprocess
import urllib.request

gaming_packages = {
    "lutris",
    "wine",
    "nvidia-settings",
    "zenity",
    "zenity-common"
}

STEAM_DEB_URL = "https://cdn.akamai.steamstatic.com/client/installer/steam.deb"
STEAM_DEB_PATH = "/tmp/steam.deb"

def download_steam():
    if os.path.exists(STEAM_DEB_PATH):
        print("[*] Steam .deb already downloaded.")
        return
    print("[*] Downloading Steam .deb installer...")
    urllib.request.urlretrieve(STEAM_DEB_URL, STEAM_DEB_PATH)
    print("[*] Download complete.")

def install_steam():
    if not os.path.exists(STEAM_DEB_PATH):
        download_steam()
    print("[*] Installing Steam package...")
    run(f"sudo dpkg -i {STEAM_DEB_PATH}")
    print("[*] Fixing dependencies...")
    run("sudo apt-get install -f -y")
    print("[*] Steam installed.")

def install():
    print("[+] Installing gaming packages...")
    install_packages(gaming_packages)
    download_steam()
    install_steam()
    os.remove(STEAM_DEB_PATH)



