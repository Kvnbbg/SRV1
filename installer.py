# installer
import pkg_resources
import subprocess
import platform
import sys

def is_package_installed(package_name):
    """Check if a Python package is installed."""
    try:
        pikppkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

def get_pip_command():
    """Return the appropriate pip command depending on the system."""
    try:
        subprocess.check_call(["pip3", "--version"])
        return "pip3"
    except subprocess.CalledProcessError:
        return "pip"

def install_package(package_name):
    """Install a Python package using pip or pip3."""
    pip_cmd = get_pip_command()
    try:
        subprocess.check_call([sys.executable, "-m", pip_cmd, "install", package_name])
        print(f"{package_name} has been installed.")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name} with normal privileges. Trying with elevated privileges...")
        try:
            if platform.system() == "Windows":
                subprocess.check_call([sys.executable, "-m", pip_cmd, "install", package_name], shell=True)
            else:
                subprocess.check_call(["sudo", sys.executable, "-m", pip_cmd, "install", package_name])
            print(f"{package_name} has been installed with elevated privileges.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package_name} even with elevated privileges. Please install it manually.")

def get_actual_package_name(package_name):
    """Try to find the actual package name in case of errors."""
    pip_cmd = get_pip_command()
    try:
        result = subprocess.check_output([pip_cmd, "search", package_name])
        lines = result.decode('utf-8').split('\n')
        for line in lines:
            if package_name in line:
                return line.split()[0]
    except Exception as e:
        print(f"Error finding actual package name for {package_name}: {e}")
    return package_name

# List of required packages
required_packages = ["pygame", "tkinter"]

for package in required_packages:
    if not is_package_installed(package):
        print(f"{package} is not installed. Installing now...")
        actual_package_name = get_actual_package_name(package)
        install_package(actual_package_name)
    else:
        print(f"{package} is already installed.")

print("Installation process completed.")
# end installer