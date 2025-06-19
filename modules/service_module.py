import os
import urllib.request
import subprocess
import shutil

def run(cmd):
    """Run a shell command and raise if it fails."""
    print(f"> {cmd}")
    subprocess.run(cmd, shell=True, check=True)


def run_ignore_errors(cmd):
    """Run a shell command but don't raise if it fails."""
    print(f"> {cmd} (ignoring errors)")
    subprocess.run(cmd, shell=True)


def install_packages(packages):
    """Install a list of packages using apt."""
    if shutil.which("apt") is None:
        raise RuntimeError("This script only supports Debian-based distros with apt.")
    run("sudo apt update")
    run("sudo apt install -y " + " ".join(packages))


def download_and_install_deb(url, deb_name=None, remove_after=True):
    """
    Downloads a .deb file from the given URL and installs it with dependency resolution.

    Args:
        url (str): The full URL to the .deb file
        deb_name (str): Optional custom file name (defaults to basename of URL)
        remove_after (bool): If True, delete the .deb file after install
    """
    # Set download path
    if deb_name is None:
        deb_name = os.path.basename(url)
    deb_path = os.path.join("/tmp", deb_name)

    # Download if not already there
    if not os.path.exists(deb_path):
        print(f"[*] Downloading {deb_name}...")
        urllib.request.urlretrieve(url, deb_path)
        print("[*] Download complete.")
    else:
        print(f"[*] {deb_name} already downloaded.")

    # Attempt install
    print("[*] Installing package...")
    run_ignore_errors(f"sudo dpkg -i {deb_path}")
    run("sudo apt-get install -f -y")
    print("[*] Package installed successfully.")

    # Clean up
    if remove_after and os.path.exists(deb_path):
        os.remove(deb_path)
        print("[*] Cleaned up installer.")