#! /usr/bin/env python3

import gi
import os
import signal
import notify2
import subprocess

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk, AppIndicator3 as AppIndicator

APPINDICATOR_ID = 'PiDisplay'

class PiDisplay(object):
  def __init__(self):
    
    ICON = 'display'  # Get default icon from /usr/share/icons/gnome/16x16/
    notify2.init(APPINDICATOR_ID)
    self.indicator = AppIndicator.Indicator.new(APPINDICATOR_ID, ICON, AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
    self.indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    self.indicator.set_menu(self.__build_menu())
    
    
  def run(self):
    gtk.main()

  def use_hdmi(self, _):
    cmd_hdmi = "./UCTRONICS_LCD_hdmi"
    p = subprocess.Popen(['sudo', cmd_hdmi], cwd=os.path.expanduser('~/UCTRONICS_LCD35_RPI/'))
    n = notify2.Notification(
      "Switching to HDMI",
      "Loading drivers then rebooting Pi. This may take a minute or two — please be patient!",
      "/usr/share/icons/Adwaita/48x48/actions/system-run.png"
    )
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(30000)
    n.show()
    p.wait()
  
  def use_lcd35(self, _):
    cmd_lcd35 = "./UCTRONICS_LCD35_install"
    p = subprocess.Popen(['sudo', cmd_lcd35], cwd=os.path.expanduser('~/UCTRONICS_LCD35_RPI/'))
    n = notify2.Notification(
      "Switching to LCD 3.5\"",
      "Loading drivers then rebooting Pi. This may take a minute or two — please be patient!",
      "/usr/share/icons/Adwaita/48x48/actions/system-run.png"
    )
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(30000)
    n.show()
    p.wait()
  
  def about(self, _):
    n = notify2.Notification(
    "About PiDisplay",
    "Utility to switch between HDMI and UCTRONIC LCD 3.5\" displays\n\nCreated for Calistoga STEM Camp Summer 2019\nBy Barry Low <barrylow@gmail.com>\nView source: https://github.com/bearcanrun/pi-display",
    "/usr/share/icons/gnome/48x48/devices/display.png"
    )
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.set_timeout(2500)
    n.show()
    
  def quit(self, _):
    notify2.uninit()
    gtk.main_quit()

  def __build_menu(self):
    menu = gtk.Menu()
    item_hdmi = gtk.MenuItem('Switch to HDMI')
    item_hdmi.connect('activate', self.use_hdmi)
    menu.append(item_hdmi)
    item_lcd35 = gtk.MenuItem('Switch to LCD 3.5"')
    item_lcd35.connect('activate', self.use_lcd35)
    menu.append(item_lcd35)
    item_about = gtk.MenuItem('About PiDisplay')
    item_about.connect('activate', self.about)
    menu.append(item_about)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', self.quit)
    menu.append(item_quit)
    menu.show_all()
    return menu
    
def main():
  signal.signal(signal.SIGINT, signal.SIG_DFL)
  app = PiDisplay()
  app.run()

if __name__ == "__main__":
  main()
