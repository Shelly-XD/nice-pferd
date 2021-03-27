# nice-pferd
Manga scans reader and downloader for when you get offline need Android+Termux phone or any Computer running python3


## Dependencies :
#### packages
* [python](https://www.python.org/)(>=3)
#### python modules (install them with *pip*)
* [flask](https://pypi.org/project/Flask/)
* [bs4](https://pypi.org/project/bs4/)
* [requests](https://pypi.org/project/requests/)

+any webBrowser

## Supported Websites : (ask me for more if you want, I will add the support)
* [kissmanga.in](https://kissmanga.in/)

## Installation

#### Install dependencies :
* ubuntu:
```sudo apt update && apt upgrade
sudo apt install python3 python3-pip ipython3
sudo apt install git
```
* arch:
```sudo pacman -S python-pip
sudo pacman -S git
```
* termux (android device):
```pkg install python
pkg install git
```

#### Install nice-pferd:
```git clone https://github.com/augustin64/nice-pferd/
cd nice-pferd/
pip install -r requirements.txt
```

#### nice-pferd is ready, to use it just run
```
flask run
```
Open `http://localhost:5000` in your favorite webbrowser
