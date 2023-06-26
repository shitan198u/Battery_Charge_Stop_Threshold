
# Setting Battery Charge Stop Threshold for ASUS Laptops on Linux using GUI

This repository contains a Python application that allows you to set the battery charge stop threshold for ASUS laptops on Linux. It provides a graphical user interface (GUI) using PyQt5 and executes a bash script to modify the threshold.
This only works for devices using `systemd` which should generally be the case

## Clone the Repository

```bash
git clone https://github.com/shitan198u/Battery_Charge_Stop_Threshold.git
cd Battery_Charge_Stop_Threshold

```
Setting the permissions
```bash
sudo chmod +x modify_threshold.sh
```

## Installation

It requires the pyqt5 package you can install from below

Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install python3-pyqt5

```
Fedora:
```bash
sudo dnf install python3-qt5

```
openSUSE:
```bash
sudo zypper install python3-qt5

```
Arch Linux:
```bash
sudo pacman -S python-pyqt5

```   
Using Pip:

You can also install PyQt5 using the `pip` package manager. Here's how:

1. First, make sure you have `pip` installed on your system. You can check if `pip` is installed by running the command `pip --version` or `pip3 --version`. If `pip` is not installed, you can install it using your distribution's package manager. For example, on Ubuntu/Debian you can run `sudo apt-get install python3-pip`.

2. Once you have `pip` installed, you can install PyQt5 by running the command `pip install PyQt5` or `pip3 install PyQt5`. This will download and install the latest version of PyQt5 from the Python Package Index.

After installing PyQt5 using `pip`, you should be able to run the PyQt5 GUI application script.

## Launching the application
once inside the ./Battery_Charge_Stop_Threshold launch using:

```bash
python3 app.py
```


## References

[Limit Battery Charging](https://www.linuxuprising.com/2021/02/how-to-limit-battery-charging-set.html)


## License

[MIT](https://choosealicense.com/licenses/mit/)

