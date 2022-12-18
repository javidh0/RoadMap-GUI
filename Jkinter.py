from tkinter import *
import pyautogui as pyg
import pandas as pd
pyg
class MainWindow:
    pass

class Formate(object):
    _font = {1: ("Consolas", 15), 2:("Consolas", 15), 'res' : ("Consolas", 15)}
    _color= {1: "grey", 2:"grey30"}
    _size = {1: 18, 2: 18}

    _Title = "RoadMap"

    _dFont= {1: "Consolas", 2:"Consolas", 'res' : "Consolas", 'res1':"Consolas"}
    _dColor= {1: "grey20", 2:"grey50", 'res' : 'Black', 'res1': 'grey30'}
    _dSize = {1: 15, 2: 12, 'res':25, 'res1':18}

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
        self.__btn = Button(tk, text=self.__name, font=self._font[self.__type], width=15)
        self.__btn['bg'] = self._color[self.__type]
        self.__btn['command'] = self.__onClick
        if self.progress > 90:
            self.__btn['bg'] = self.completed['colour']
        return self.__btn
    def getData(self) -> list:
        return [self.__name, self.progress, self.__About]
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
        self.__btn = Button(tk, text=self.__name, font=self._font[self.__type], width=15)
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
    __toolFrm = None
    __desFrm = None
    __rdFrm = None
    __obj = None

    def __init__(self, objlist) -> None:
        self.__rt = Tk()
        self.__rt.geometry("1000x1000")
        self.__rt.title(self._Title)
        width = self.__rt.winfo_screenwidth() - 50
        height = self.__rt.winfo_screenheight() - 50
        self.__rt.geometry('%dx%d'%(width, height))
        self.__obj = objlist
        self.__sel = objlist[2]

    def __clrScr(self):
        for x in self.__rt.winfo_children():
            x.destroy()
    
    def __edit(self):
        print("edit")
    def __editD(self):
        print("edit des")
    def __p(self, i:int = 10):
        print("progress "+str(i))
    def __save(self):
        print("Save")
    def __open(self):
        print("Open")
    
    def RoadMapWindow(self):
        self.__clrScr()
        self.__desFrm = LabelFrame(self.__rt)
        self.__desFrm.place(relx=0.01, rely=0.01, relheight=0.48, relwidth=0.38, anchor=NW)
        self.__toolFrm= LabelFrame(self.__rt)
        self.__toolFrm.place(relx=0.01, rely=0.98, relheight=0.48, relwidth=0.38, anchor=SW)
        self.__rdFrm = LabelFrame(self.__rt)
        self.__rdFrm.place(relx=0.98, rely=0.98, relheight=0.96, relwidth=0.58, anchor=SE)

        Button(self.__toolFrm, text="+5%", font=self._font['res'], width=20, command=lambda:self.__p(5)).pack(pady=10)
        Button(self.__toolFrm, text="+10%", font=self._font['res'], width=20, command=self.__p).pack(pady=10)
        Button(self.__toolFrm, text="Edit Name%", font=self._font['res'], width=20, command=self.__edit).pack(pady=10)
        Button(self.__toolFrm, text="Edit Descrpition", font=self._font['res'], width=20, command=self.__editD).pack(pady=10)
        Button(self.__toolFrm, text="Save", font=self._font['res'], width=20, command=self.__save).pack(pady=10)
        Button(self.__toolFrm, text="Open", font=self._font['res'], width=20, command=self.__open).pack(pady=10)
        self.__refresh()

    def __refresh(self, op:int = 1) -> None:
        if(op==1):  #Refresh Description
            for wid in self.__desFrm.winfo_children():
                wid.destroy()
            dta = self.__sel.getData()
            Label(self.__desFrm, text=str(dta[0]), font=(self._dFont['res'], self._dSize['res'])).pack(anchor=W,pady=20, padx=5)
            Label(self.__desFrm, text="Progress "+ str(dta[1]) +"%", font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
            Label(self.__desFrm, text= str(dta[2]), font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
            
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
