import subprocess
import shutil

def run(cmd):
    """Run a shell command and raise if it fails."""
    print(f"> {cmd}")
    subprocess.run(cmd, shell=True, check=True)


def install_packages(packages):
    """Install a list of packages using apt."""
    if shutil.which("apt") is None:
        raise RuntimeError("This script only supports Debian-based distros with apt.")
    run("sudo apt update")
    run("sudo apt install -y " + " ".join(packages))