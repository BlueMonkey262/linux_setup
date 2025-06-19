#!/usr/bin/env python3
import dbus

from modules import service_module

from modules import kde, gaming, core, development

def main():
    kde_mod = input("[+] Modify KDE? [y/n]")
    if kde_mod == "y":
        wallpaper_path = "wallpaper.jpg"
        kde.set_kde_wallpaper(wallpaper_path)
        kde.enable_dark_mode()
        print("Done.")
    gamingPackages = input("[+] Install Gaming Packages? [y/n]")
    if gamingPackages == "y":
        gaming.install()
        print("Done.")
    corePackages = input("[+] Install Core Packages? [y/n]")
    if corePackages == "y":
        core.install()
        print("Done.")
    devPackages = input("[+] Install Development Packages? [y/n]")
    if devPackages == "y":
        development.install()
        print("Done.")

if __name__ == "__main__":
    main()
