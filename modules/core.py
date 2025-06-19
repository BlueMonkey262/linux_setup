from .service_module import run, install_packages

def install():
    general_packages = {
        "btop",
        "htop",
        "curl",
        "wget"
    }
    install_packages(general_packages)
