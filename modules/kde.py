from pathlib import Path
import dbus
from .service_module import run, install_packages
import os

def set_kde_wallpaper(filepath, plugin='org.kde.image'):
    """Sets the wallpaper in KDE Plasma via dbus."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Wallpaper not found: {filepath}")

    abs_path = os.path.abspath(filepath)
    file_url = f"file://{abs_path}"

    jscript = f"""
    var allDesktops = desktops();
    for (i=0;i<allDesktops.length;i++) {{
        d = allDesktops[i];
        d.wallpaperPlugin = "{plugin}";
        d.currentConfigGroup = Array("Wallpaper", "{plugin}", "General");
        d.writeConfig("Image", "{file_url}");
    }}
    """

    # Send to plasma shell over dbus
    bus = dbus.SessionBus()
    plasma = dbus.Interface(
        bus.get_object('org.kde.plasmashell', '/PlasmaShell'),
        dbus_interface='org.kde.PlasmaShell'
    )
    print("[+] Sending wallpaper script to PlasmaShell via DBus...")
    plasma.evaluateScript(jscript)

def enable_dark_mode():
    print("[+] Applying KDE dark mode...")

    # Apply the full Breeze Dark look-and-feel
    run("lookandfeeltool -a org.kde.breezedark.desktop")

    # Restart plasmashell to apply changes immediately

