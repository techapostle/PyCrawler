# This script is used to install the required pip packages for the crawler.
# The script first checks if pip3 is installed, and if not, it warns the user and exits.
# The script then asks if the user wants to install the packages using pip3 or pipx.
# If the user chooses pip3, the script installs the packages using subprocess.
# If the user chooses pipx, the script checks if pipx is installed, and if not, it warns the user and exits, otherwise, it installs the packages using pipx.
# If pipx is chosen, the script will create a virtual environment in the current directory called venv, and install the packages in the virtual environment.
# After the pipx installation, the user is told to activate the virtual environment using the command source venv/bin/activate.

import subprocess
import sys


def install_requirements():
    try:
        subprocess.run(["pip3", "--version"], check=True)
    except FileNotFoundError:
        print("pip3 is not installed. Please install pip3 to continue.")
        sys.exit(1)

    print("Do you want to install the required packages using pip3 or pipx?")
    choice = input("Enter 'pip3' or 'pipx': ")

    if choice == "pip3":
        print("Installing packages using pip3...")
        (
            print("Packages installed successfully.")
            if subprocess.run(
                ["pip3", "install", "-r", "requirements.txt"], check=True
            ).returncode
            == 0
            else print("Failed to install packages.")
        )
    elif choice == "pipx":
        try:
            subprocess.run(["pipx", "--version"], check=True)
        except FileNotFoundError:
            print("pipx is not installed. Please install pipx to continue.")
            sys.exit(1)
        # Check if virtualenv is installed
        try:
            subprocess.run(["pipx", "run", "virtualenv", "--version"], check=True)
        except FileNotFoundError:
            print("virtualenv is not installed. Please install virtualenv to continue.")
            sys.exit(1)
        print("Creating virtual environment...")
        if subprocess.run(["pipx", "run", "virtualenv", "venv"]).returncode == 0:
            print("Virtual environment created successfully. Installing packages...")
        else:
            print("Failed to create virtual environment.")
            sys.exit(1)
        (
            print(
                "Packages installed successfully. Please activate the virtual environment using the command 'source venv/bin/activate'."
            )
            if subprocess.run(
                ["pipx", "run", "venv", "pip3", "install", "-r", "requirements.txt"],
                check=True,
            ).returncode
            == 0
            else print("Failed to install packages.")
        )
    else:
        print("Invalid choice. Please enter 'pip3' or 'pipx'.")
        sys.exit(1)
