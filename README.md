# nice-pferd
Manga scans reader and downloader for when you get offline need Android+Termux phone or any Computer running python3


## Dependencies :
#### packages
* [python](https://www.python.org/)(>=3)
#### python modules
* [flask](https://pypi.org/project/Flask/)
* [bs4](https://pypi.org/project/bs4/)
* [requests](https://pypi.org/project/requests/)

+any webBrowser

## Supported Websites : (ask me for more if you want, I will add the support)
* [kissmanga.in](https://kissmanga.in/)

## Installation

#### Install dependencies :
* ubuntu:
```
sudo apt update && apt upgrade
sudo apt install python3 python3-pip ipython3
sudo apt install git
```
* Arch Linux:
```
sudo pacman -S python-pip
sudo pacman -S git
```
* termux (android device):
```
pkg install python
pkg install git
```

#### Install nice-pferd:
```
git clone https://github.com/augustin64/nice-pferd.git
nice-pferd/install.sh
```

#### nice-pferd is ready, to use it :

Just run `nice-pferd` every time you want to use it  
Open `http://localhost:5000` in your favorite webbrowser

### To upgrade your nice-pferd version
Use `nice-pferd-upgrade`, it will delete all your files and custom URLs but will pull the new commits to your machine
