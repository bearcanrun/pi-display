# PiDisplay

PiDisplay is a system tray utility built for Raspberry Pi for switching between HDMI and UCTRONICS 3.5" LCD displays. The default method involves running bash scripts in the terminal, so PiDisplay simplifies this process by putting simple options in a dropdown menu from the system tray.

> This app is build specifically for this [UCTRONICS screen](https://github.com/UCTRONICS/UCTRONICS_LCD35_RPI)

The script was initially develope directly on the Pi with [UC Davis's c-STEMBian](https://c-stem.ucdavis.edu/c-stembian/download-2/) installed. c-STEMBian is a curated OS built on Raspbian with a wide selection of c-STEM packages.

## Development

Tracking down dependencies for the various Python environments can be challenging.

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

To build ryb:
```
python setup.py sdist --formats=gztar
```

## About

This utility was inspired by and created for the Calistoga STEM Camp Summer 2019.