import tkinter as tk
from tkinter import messagebox, font
import json
import csv
import os

gestureList = []
with open('model\keypoint_classifier\keypoint_classifier_label.csv', encoding='utf-8-sig') as f:
    for line in f:
        gestureList.append(line.rstrip())
    print(gestureList)
allApplianceList = []

combo_map = {}
def readFilesInFolder(folderPath):
    loadedDict = {}
    jsonOnTuple = ()
    jsonOffTuple = ()
    try: 
        for fileName in os.listdir(folderPath):
            filePath = os.path.join(folderPath, fileName)
            if os.path.isfile(filePath):
                with open(filePath, 'r') as f:
                    loadedDict = json.load(f)
                    for key, value in loadedDict.items():
                        if key == "on":
                           if type(value) == list:
                                for gesture in value:
                                    jsonOnTuple = jsonOnTuple + tuple(gesture.split())
                        if key == "off":
                           if type(value) == list:
                                for gesture in value:
                                    jsonOffTuple = jsonOffTuple + tuple(gesture.split())
    except FileNotFoundError:
        print(f"Error: Folder {folderPath} not found.")
        return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None
    
    finalList = [loadedDict, jsonOnTuple, jsonOffTuple]
    return finalList

class tkinterWin(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HomePage, CreatePage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.titleBar(controller)
        '''settings = readFilesInFolder("user_settings")
        print(settings)'''
        self.configure(bg="#92b6f0")

        testL = tk.Label(self, text="test")
        testL.grid(row=1, column=0, pady=30)

    def titleBar(self, controller):
        titleFrame = tk.Frame(self, height=40, width=800, bg="#92b6f0")
        titleFrame.grid(row=0, column=0)

        homeButton = tk.Button(titleFrame, text="Home",
                               command = lambda : controller.show_frame(HomePage))
        createButton = tk.Button(titleFrame, text="New",
                                 command = lambda : controller.show_frame(CreatePage))
        homeButton.grid(row=0, column=0)
        createButton.grid(row=0, column=1)

        

class CreatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.titleBar(controller)

        mainCreateFrame = tk.Frame(self, height=560, width=800)
        mainCreateFrame.grid(row=1, column=1)
        mainCreateFrame.configure(bg="#92b6f0")

        self.configure(bg="#92b6f0")

        nameL = tk.Label(mainCreateFrame, text="Name of appliance")
        nameL.grid(row=1, column=0, pady=0)
        nameL.configure(bg="#92b6f0")

        applianceNameVar = tk.StringVar()
        nameE = tk.Entry(mainCreateFrame, textvariable=applianceNameVar)
        nameE.grid(row=2, column=0, padx=50)

        tokenL = tk.Label(mainCreateFrame, text="Access Token")
        tokenL.grid(row=1, column=2, padx=20)
        tokenL.configure(bg="#92b6f0")

        tokenIDVar = tk.StringVar()
        tokenE = tk.Entry(mainCreateFrame, textvariable=tokenIDVar)
        tokenE.grid(row=2, column=2, padx=50)

        onTitleL = tk.Label(mainCreateFrame, text="On Gestures")
        onTitleL.grid(row=3, column=0, pady=(50,0))
        onTitleL.configure(bg="#92b6f0")

        onInstruct = tk.Label(mainCreateFrame, text="Seperate gestures by space")
        onInstruct.grid(row=4, column=0)
        onInstruct.configure(bg="#92b6f0")

        onGesturesVar = tk.StringVar()
        onGestureE = tk.Entry(mainCreateFrame, textvariable=onGesturesVar)
        onGestureE.grid(row=5, column=0)

        offTitleL = tk.Label(mainCreateFrame, text="Off Gestures")
        offTitleL.grid(row=3, column=2, pady=(50,0))
        offTitleL.configure(bg="#92b6f0")

        offInstruct = tk.Label(mainCreateFrame, text="Seperate gestures by space")
        offInstruct.grid(row=4, column=2)
        offInstruct.configure(bg="#92b6f0")

        offGesturesVar = tk.StringVar()
        offGestureE = tk.Entry(mainCreateFrame, textvariable=offGesturesVar)
        offGestureE.grid(row=5, column=2)

        mainCreateFrame.columnconfigure(1, weight=2)

        saveButton = tk.Button(mainCreateFrame, text="Save", command= lambda : self.saveGesture(applianceNameVar, tokenIDVar, onGesturesVar, offGesturesVar))
        saveButton.grid(row=6, column=1, pady=(50,0))

        self.errorL = tk.Label(mainCreateFrame, text="")
        self.errorL.grid(row=7, column=1)
        self.errorL.config(bg="#92b6f0", fg="red")

    def titleBar(self, controller):
        titleFrame = tk.Frame(self, height=40, width=800, bg="#92b6f0")
        titleFrame.grid(row=0, column=0)

        homeButton = tk.Button(titleFrame, text="Home",
                               command = lambda : controller.show_frame(HomePage))
        createButton = tk.Button(titleFrame, text="New",
                                 command = lambda : controller.show_frame(CreatePage))
        homeButton.grid(row=0, column=0)
        createButton.grid(row=0, column=1)

    def saveGesture(self, applianceNameVar, tokenIDVar, onGesturesVar, offGesturesVar):
        applianceName = applianceNameVar.get()
        tokenID = tokenIDVar.get()
        onGestures = onGesturesVar.get()
        onGestures = onGestures.split()
        offGestures = offGesturesVar.get()
        offGestures = offGestures.split()

        flag = False
        for word in onGestures:
            if not(word in gestureList):
                flag = True
        
        for word in offGestures:
            if not(word in gestureList):
                flag = True

        if flag:
            self.errorL.config(text="Error with gesture entry")
            print("That was not a correct gesture!")
        else:        
            onGestureTuple = ()
            for gesture in onGestures:
                onGestureTuple = onGestureTuple + tuple(gesture.split())
            
            offGestureTuple = ()
            for gesture in offGestures:
                offGestureTuple = offGestureTuple + tuple(gesture.split())

            json_dict = {
                "name" : applianceName,
                "token" : tokenID,
                "on" : onGestureTuple,
                "off" : offGestureTuple,
            }
            with open("user_settings/lightbulb.json", "w") as f:
                json.dump(json_dict, f)

            self.errorL.config(fg="black", text="Appliance saved successfully")

root = tkinterWin()
root.title("Gesture Home")
root.geometry("800x600")
root.configure(bg="#92b6f0")  # Soft blue background

title_font = font.Font(family="Helvetica", size=20, weight="bold")
section_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=11)

root.mainloop()

print(readFilesInFolder("user_settings"))