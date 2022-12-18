from tkinter import *
import pyautogui as pyg
import pandas as pd
pyg
class MainWindow:
    pass

class Formate(object):
    _font = {1: "Consolas", 2:"Consolas"}
    _color= {1: "grey", 2:"grey30"}
    _size = {1: 15, 2: 15}

    _Title = "RoadMap"

    _dFont= {1: "Consolas", 2:"Consolas"}
    _dColor= {1: "grey20", 2:"grey50"}
    _dSize = {1: 15, 2: 12}

    completed = {'colour' : 'green'}

class SubTask(Formate):
    __name = None
    __About = None
    progress = None
    __type = None
    __btn = None
    def __init__(self, title:str = "Unknown Task", Note:str = "", progress:int = 0, type:int = 1) -> None:
        self.__name = title
        self.__About = Note
        self.progress = progress
        self.__type = type

    def __onClick(self, win:MainWindow):
        return self

    def create(self, tk):
        self.__btn = Button(tk, text=self.__name, font=(self._font[self.__type], self._size[self.__type]), width=15)
        self.__btn['bg'] = self._color[self.__type]
        self.__btn['command'] = self.__onClick
        if self.progress > 90:
            self.__btn['bg'] = self.completed['colour']
        return self.__btn

    def edit():
        pass

    def save_in_file():
        pass

class RoadMap(Formate):
    __subtask = []
    __name = None
    __progress = None
    __btn = None
    __type = None
    __sum = 0
    def __init__(self, task:list[SubTask], name:str, type:int = 1) -> None:
        self.__subtask = task
        self.__name = name
        self.__type = type
        for x in self.__subtask:
            self.__sum += x.progress
        self.__progress = self.__sum // len(self.__subtask)

    def create(self, tk):
        self.__btn = Button(tk, text=self.__name, font=(self._font[self.__type], self._size[self.__type]), width=15)
        self.__btn['text'] += (" "+str(self.__progress))
        return self.__btn
    
    def getTask(self):
        return self.__subtask

    def onClick(self):
        pass

class Data:
    __file = "data\data.csv"
    __df = pd.read_csv(__file)
    def initialize(self) -> list[RoadMap]:
        TskObj = dict()
        toReturn = []
        for indx in range(self.__df.shape[0]):
            row = self.__df.iloc[indx]
            if not row['RoadMap'] in list(TskObj.keys()):
                TskObj[row['RoadMap']] = []
            obj = SubTask(row['Task'], row['About'], row['Progress'], row['Type'])
            TskObj[row['RoadMap']].append(obj)
        for tsk in TskObj.keys():
            temp = RoadMap(TskObj[tsk], tsk)
            toReturn.append(temp)
        return toReturn

class MainWindow(Formate):
    __rt = None
    __sel:SubTask= None

    def __init__(self) -> None:
        self.__rt = Tk()
        self.__rt.geometry("1000x1000")
        self.__rt.title(self._Title)
        width = self.__rt.winfo_screenwidth() - 50
        height = self.__rt.winfo_screenheight() - 50
        self.__rt.geometry('%dx%d'%(width, height))

    def __clrScr(self):
        for x in self.__rt.winfo_children():
            x.destroy()
    def RoadMapWindow(self):
        self.__clrScr()
        desFrm = LabelFrame(self.__rt)
        desFrm.place(relx=0.01, rely=0.01, relheight=0.48, relwidth=0.38, anchor=NW)
        toolFrm= LabelFrame(self.__rt)
        toolFrm.place(relx=0.01, rely=0.98, relheight=0.48, relwidth=0.38, anchor=SW)
        rdFrm = LabelFrame(self.__rt)
        rdFrm.place(relx=0.98, rely=0.98, relheight=0.96, relwidth=0.58, anchor=SE)

    def Select(self, obj:SubTask):
        self.__sel = obj
        
    def Enable(self):
        self.__rt.mainloop()
        

class Window:
    __frm:Frame = None
    __title = None
    __state = False

    def __init__(self, frm:Frame, title) -> None:
        self.__frm = frm
        self.__title = title

class Security:
    pass

class EncryptDta:
    __key = b'SzwHFgWh4A6xjZlBHHNCM0JkDaq2l8sBiLMX7Tq_MHc='
