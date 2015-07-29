import pip
import subprocess


for distribution in pip.get_installed_distributions():
    subprocess.call("pip install --upgrade " + distribution.project_name, shell=True)