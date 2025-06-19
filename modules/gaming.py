from .service_module import run, install_packages, download_and_install_deb

gaming_packages = {
    "lutris",
    "wine",
    "nvidia-settings",
    "zenity",
    "zenity-common"
}

def install():
    install_packages(gaming_packages)
    steam_url = "https://cdn.akamai.steamstatic.com/client/installer/steam.deb"
    download_and_install_deb(steam_url)



