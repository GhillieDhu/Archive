import wx

class controlPanel(wx.Panel):
    def __init__(self, parent, startF, stopF, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        StartButton = wx.Button(self, label="Start")
        StartButton.Bind(wx.EVT_BUTTON, startF)
        StopButton = wx.Button(self, label="Stop")
        StopButton.Bind(wx.EVT_BUTTON, stopF)
        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(StartButton, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        Sizer.Add(StopButton, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        self.SetSizerAndFit(Sizer)

class controlFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        startF = kwargs.pop("startF")
        stopF = kwargs.pop("stopF")
        wx.Frame.__init__(self, *args, **kwargs)
        self.Panel = controlPanel(self, startF, stopF)
        self.Fit()

    def OnQuit(self, event=None):
        self.Close()

def new(startF, stopF):
    app = wx.App()
    frame = controlFrame(None, startF=startF, stopF=stopF)
    frame.Show()
    app.MainLoop()
    return frame

if __name__ == '__main__':
    app = wx.App()
    frame = controlFrame(None, startF=lambda event: 0, stopF=lambda event: 0)
    frame.Show()
    app.MainLoop()
