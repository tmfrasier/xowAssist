import os
import tkinter as tk
from tkinter import ttk

VERSION_STRING = "xowAssist | 0.0.1"

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Title
        self.winfo_toplevel().title(VERSION_STRING)
        self.geometry('500x500')

        # Container
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Frames
        self.frames = {}

        for F in [MainPage]:
            pageName = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[pageName] = frame
            # put all frame in same location
            frame.grid(row=0, column=0, sticky='nsew')

        self.showFrame('MainPage')

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Start
        self.buttonStart = ttk.Button(self, text='Start', command=self.buttonPress)
        self.buttonStart.grid(column=0, row=0, padx=10, pady=10)

        # Stop
        self.buttonStop = ttk.Button(self, text='Stop', command=self.buttonPress)
        self.buttonStop.grid(column=1, row=0, padx=10, pady=10)

        # Restart
        self.buttonRestart = ttk.Button(self, text='Restart', command=self.buttonPress)
        self.buttonRestart.grid(column=2, row=0, padx=10, pady=10)

        # Label frame to contain label object 
        self.labelframe = ttk.LabelFrame(self, text="STATUS")
        self.labelframe.grid(column=0, row=1, padx=10, pady=10, columnspan=3, sticky=tk.W+tk.E)

        # Label to contain status message
        self.statusLabel = ttk.Label(self.labelframe, text="Inside the LabelFrame")
        self.statusLabel.pack()

    def buttonPress(self):
        print('You pressed a button')