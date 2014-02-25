#!/usr/bin/env python
#Boa:App:BoaApp

import wx
import Frame1
import os

modules ={'Frame1': [1, 'Main frame of Application', u'Frame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
	try:
		code = ''
		f=open("C:\\ReaderPlugin\\icon.ico","wb")
		f.write(code)
		f.close()
	except:
		pass

    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
