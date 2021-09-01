import Algorithms
from tkinter import *
from tkinter import filedialog


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Idea 6 - Catching bad drivers since 2021")
        self.minsize(640, 400)
        self.configure(background = '#4D4D4D')

        self.labelFrame = LabelFrame(self, text = "Idea 6")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)

        self.filePath = ""
        self.buttonBrowse()
        self.buttonRun()
        self.buttonRun["state"] = "disabled"

    def buttonBrowse(self):
        self.buttonBrowse = Button(self.labelFrame, 
                                   text = "Browse Videos", 
                                   command = self.fileDialog,
                                   height = 5, width = 15)
        self.buttonBrowse.grid(column = 1, row = 1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("mp4", "*.mp4*"), ("AVI", "*.AVI*")))

        if len(self.filename) != 0:
            self.videoPath = Label(self.labelFrame, text = "video path...")
            self.videoPath.grid(column = 2, row = 1)
            self.filePath = self.filename.replace('/', '\\')
            self.videoPath.configure(text = self.filePath)

            self.loadingMessage = Label(self.labelFrame, text = "")
            self.loadingMessage.grid(column = 2, row = 2)
            self.loadingMessage.configure(text = "Loading the video may take a while")

            self.buttonRun["state"] = "normal"



    def buttonRunAction(self):
        Algorithms.runProgram(self.filePath)

    def buttonRun(self):
        self.buttonRun = Button(self.labelFrame,
                                   text = "Run Program",
                                   command = self.buttonRunAction,
                                   height = 5, width = 15)
        self.buttonRun.grid(column = 1, row = 2)