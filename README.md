# nice-pferd
Manga scans reader and downloader


## Dependencies :
#### Packages
* [python](https://www.python.org/)
* [git](https://git-scm.com/)

#### python modules
* [flask](https://pypi.org/project/Flask/)
* [bs4](https://pypi.org/project/bs4/)
* [requests](https://pypi.org/project/requests/)

\+ any webBrowser

## Supported Websites : (ask me for more if you want, I will add the support)
* [kissmanga.in](https://kissmanga.in/)

## Installation

#### Install dependencies :
* ubuntu:
```
apt update && apt upgrade
apt install python3 python3-pip ipython3
apt install git
```
* Arch Linux:
```
pacman -S python-pip
pacman -S git
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

## Features :
+ Updates Notifier (includes changelogs)
+ Multiple mangas downloader
+ Easier installation script
+ Free & Open Source (feel free to contribute)
+ Dark/Light themes

### [WIP] 
+ support for [mangamelon](http://mangamelon.com)

### [TODO]
+ Store files outside of the GitHub project (so files aren't wiped out when nicepferd is upgraded)
+ Add more websites
+ Configuration file
