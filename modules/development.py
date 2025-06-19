import os
import urllib.request
import tarfile
import subprocess
import tempfile
import shutil

from .service_module import run

TOOLBOX_URL = "https://download.jetbrains.com/toolbox/jetbrains-toolbox-2.2.2.20090.tar.gz"
INSTALL_DIR = os.path.expanduser("~/.local/opt/jetbrains-toolbox")  # Choose any persistent path
TOOLBOX_BIN = os.path.join(INSTALL_DIR, "jetbrains-toolbox")

def install_jetbrains_toolbox():
    print("[*] Installing JetBrains Toolbox...")

    # Create temp directory
    with tempfile.TemporaryDirectory() as tmpdir:
        archive_path = os.path.join(tmpdir, "toolbox.tar.gz")

        # Download archive
        print("[*] Downloading...")
        urllib.request.urlretrieve(TOOLBOX_URL, archive_path)
        print("[*] Download complete.")

        # Extract archive
        print("[*] Extracting...")
        with tarfile.open(archive_path) as tar:
            tar.extractall(path=tmpdir)

        # Find the extracted folder (it's random)
        extracted_dir = next(
            os.path.join(tmpdir, d)
            for d in os.listdir(tmpdir)
            if os.path.isdir(os.path.join(tmpdir, d)) and "jetbrains-toolbox" in d
        )

        # Move to install directory
        if os.path.exists(INSTALL_DIR):
            shutil.rmtree(INSTALL_DIR)
        shutil.move(extracted_dir, INSTALL_DIR)

    # Run toolbox once to let it self-install
    bin_path = os.path.join(INSTALL_DIR, "jetbrains-toolbox")
    print(f"[*] Launching JetBrains Toolbox from {bin_path}")
    subprocess.Popen([bin_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("[✓] JetBrains Toolbox launched. Look for the icon in your system tray.")

def install():
    print("[*] Installing Toolbox...")
    install_jetbrains_toolbox()