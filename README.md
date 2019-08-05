# PiDisplay

PiDisplay is a system tray utility built for Raspberry Pi for switching between HDMI and UCTRONICS 3.5" LCD displays. The default method involves running bash scripts in the terminal, so PiDisplay simplifies this process by putting simple options in a dropdown menu from the system tray.

> This app is build specifically for this [UCTRONICS screen](https://github.com/UCTRONICS/UCTRONICS_LCD35_RPI)

The script was initially develope directly on the Pi with [UC Davis's c-STEMBian](https://c-stem.ucdavis.edu/c-stembian/download-2/) installed. c-STEMBian is a curated OS built on Raspbian with a wide selection of c-STEM packages.

## Development

Tracking down dependencies for the various Python environments can be challenging.
### Getting started
```
git clone https://github.com/bearcanrun/pi-display.git
cd pi-display
```

### Raspberry Pi w c-STEMBian

Install dependencies as follows:
Upgrade to latest PIP:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
Install GTK3+ and AppIndicator
```
sudo apt-get install python3-gi python-appindicator
pip install gobject PyGObject notify2
```
#### Notes:

- Icons located in `/usr/share/icons/`

### MacOS X (>=10.12)

Install dependencies as follows:
Upgrade to latest PIP:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
Install GTK3+ and AppIndicator
```
brew install gtk+3 pygobject3
pip3 install notify2
```

## Production

#### Standalone Binary
Note tha pyinstaller only creates binaries for the specific architecture running it. So to create a Raspbian binary, it must be done on the Raspberry Pi.

Install pyinstaller and upx
```
pip3 install --user pyinstaller
sudo apt-get install upx-ucl
```

Build
```
python3.5 -m PyInstaller ./python/pi-display/PiDisplay.py --onefile --upx-dir /usr/bin 
```

#### PyPi package

Creat Source Dist:
```
python3 setup.py sdist
```

To build run:
```
python3 setup.py sdist --formats=gztar
```

If you haven't already, register an account on [PiPy](https://pypi.org/)

For uploading dist bundle, install [twine](https://github.com/pypa/twine) (secure replacement for `setup.py upload`):
```
pip install --user --upgrade twine
```
Test package upload:
```
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Upload dist:
```
python3 -m twine upload dist/*
```

## About

The development of this utility was inspired by the Calistoga STEM Camp Summer 2019.