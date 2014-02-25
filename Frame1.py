# -*- coding: gbk -*-
#Boa:Frame:Frame1

import wx
import threading
import sgk

global mself

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(731, 333), size=wx.Size(387, 468),
              style=wx.DEFAULT_FRAME_STYLE, title='GDH')
        self.SetClientSize(wx.Size(371, 430))
        self.SetBackgroundColour(wx.Colour(254, 248, 224))
        self.SetToolTipString('')

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(64, 72), size=wx.Size(232, 22), style=0,
              value='')
        self.textCtrl1.SetToolTipString('\xc7\xeb\xca\xe4\xc8\xeb..')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(64, 104), size=wx.Size(232, 240),
              style=wx.TE_MULTILINE, value='')
        self.textCtrl2.SetToolTipString('')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label='\xcb\xd1\xcb\xf7', name='button1', parent=self,
              pos=wx.Point(64, 360), size=wx.Size(232, 32), style=0)
        self.button1.SetToolTipString('')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='GDH \xd0\xa1\xd6\xfa\xca\xd6', name='staticText1',
              parent=self, pos=wx.Point(112, 24), size=wx.Size(128, 25),
              style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, '\xbb\xaa\xce\xc4\xe7\xfa\xe7\xea'))

    def __init__(self, parent):
        global mself
        self._init_ctrls(parent)
        mself = self

    def OnButton1Button(self, event):
        self.textCtrl2.SetValue("请等待...")
        t = MyThread()
        t.start()
        event.Skip()




class MyThread(threading.Thread):
    
    def run(self):
        key = mself.textCtrl1.GetValue().encode("gbk")
        rs = sgk.get_rs(key)
        wx.MessageBox("该软件为测试版")
        txt = ""
        for r in rs:
            if len(r) > 2:
                r = r[:2] + "*" + r[3:]
            txt += r + "\n"
        #txt = "\n".join(rs)
        mself.textCtrl2.SetValue(txt)
        



