from tkinter import *
import pyautogui as pyg
import pandas as pd
import string, random
pyg
class MainWindow:
    pass

class Selected:
    __sel = None
    __win:MainWindow = None
    def initialize(self, win:MainWindow, obj):
        self.__win = win
        self.__sel = obj
    def get(self):
        return self.__sel
    def set(self, obj, ref = True):
        self.__sel = obj
        if ref:
            self.__win.refresh(1)
        if not ref:
            self.__win.refresh(0)

Selector = Selected()

class Formate(object):
    _font = {1: ("Consolas", 15), 2:("Consolas", 15), 'res' : ("Consolas", 15), 'res1':("Consolas", 25)}
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
    __hash:str = None
    def __init__(self, title:str = "Unknown Task", Note:str = "", progress:int = 0, type:int = 1, hash:str = "") -> None:
        self.__name = title
        self.__About = Note
        self.progress = progress
        self.__type = type
        self.__hash = hash

    def __onClick(self):
        Selector.set(self)
    def change(self, title:str = __name , Note:str = __About, progress:int = progress, type:int = __type):
        self.__name = title
        self.__About = Note
        self.progress = progress
        self.__type = type

    def create(self, tk):
        self.__btn = Button(tk, text=self.__name, font=self._font[self.__type], width=15)
        self.__btn['bg'] = self._color[self.__type]
        self.__btn['command'] = self.__onClick
        if self.progress > 90:
            self.__btn['bg'] = self.completed['colour']
        return self.__btn
    def getData(self) -> list:
        return [self.__name, self.progress, self.__About, self.__hash]
    def edit(self, name = __name, about = __About, prog = progress, type = __type):
        self.__name = name
        self.__About= about
        self.progress= prog
        self.__type = type
    def getIndex(self):
        return self.__hash
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
    def reWrite(self, df:pd.DataFrame):
        df.to_csv(self.__file, index=True)
    def initialize(self) -> list[RoadMap]:
        __df = pd.read_csv(self.__file)
        TskObj = dict()
        toReturn = []
        for indx in range(__df.shape[0]):
            row = __df.iloc[indx]
            if not row['RoadMap'] in list(TskObj.keys()):
                TskObj[row['RoadMap']] = []
            obj = SubTask(row['Task'], row['About'], row['Progress'], row['Type'], row['Hash'])
            TskObj[row['RoadMap']].append(obj)
        for tsk in TskObj.keys():
            temp = RoadMap(TskObj[tsk], tsk)
            toReturn.append(temp)
        return toReturn
    def Save(obj:SubTask):
        pass
    def getHash(self):
        __df = pd.read_csv(self.__file)
        return tuple(__df['Hash'])
    def increment(self, x:int, obj:SubTask):
        df = pd.read_csv(self.__file)
        df.set_index('Hash' , inplace=True)
        
        buf = df.loc[obj.getIndex()]
        buf['Progress'] = buf['Progress'] + x
        df.loc[obj.getIndex()] = buf
        self.reWrite(df)

        obj.change(buf['Task'], buf['About'], buf['Progress'], buf['Type'])
    def EditName(self, s:str, obj:SubTask):
        df = pd.read_csv(self.__file)
        df.set_index('Hash' , inplace=True)

        buf = df.loc[obj.getIndex()]
        buf['Task'] = s
        df.loc[obj.getIndex()] = buf
        self.reWrite(df)

        obj.change(buf['Task'], buf['About'], buf['Progress'], buf['Type'])
    def EditDes(self, s:str, obj:SubTask):
        df = pd.read_csv(self.__file)
        df.set_index('Hash' , inplace=True)

        buf = df.loc[obj.getIndex()]
        buf['About'] = s
        df.loc[obj.getIndex()] = buf
        self.reWrite(df)

        obj.change(buf['Task'], buf['About'], buf['Progress'], buf['Type'])
        
class MainWindow(Formate):
    __rt = None
    __toolFrm = None
    __desFrm:LabelFrame = None
    __rdFrm = None
    __RdMap:RoadMap = None
    __oobj:list[SubTask]=None
    __obj:list[SubTask] = None
    __ent:Entry = None
    __start:int = 0
    __end:int = 7
    __save_btn:Button = None
    __desBx:Text = None
    
    def __init__(self, obj:RoadMap) -> None:
        self.__rt = Tk()
        self.__rt.geometry("1000x1000")
        self.__rt.title(self._Title)
        width = self.__rt.winfo_screenwidth() - 50
        height = self.__rt.winfo_screenheight() - 50
        self.__rt.geometry('%dx%d'%(width, height))
        objlist = obj.getTask()
        self.__RdMap = obj
        self.__oobj = objlist
        self.__obj = objlist[:7]
        Selector.initialize(self, objlist[0])
        self.__ent = Entry(self.__desFrm, width=25, font=(self._dFont['res'], self._dSize['res']))
        self.__desBx = Text(self.__desFrm, width=25, font=(self._dFont['res'], self._dSize['res']))
        self.__rt.bind('<Up>',lambda event:self.__Up())
        self.__rt.bind('<Down>',lambda event:self.__Down())
    def __Down(self):
        if(self.__end == len(self.__oobj)+1):
            return None
        self.__start+=1
        self.__end+=1
        self.__obj = self.__oobj[self.__start: self.__end]
        self.refresh(op=0)

    def __Up(self):
        if(self.__start == 0):
            return None
        self.__start-=1
        self.__end-=1
        self.__obj = self.__oobj[self.__start: self.__end]
        self.refresh(op=0)
    
    def ChangeRd(self, obj:RoadMap):
        self.__RdMap = obj
        objlist = obj.getTask()
        self.__obj = objlist
        Selector.set(objlist[0], False)
    
    def __clrScr(self):
        for x in self.__rt.winfo_children():
            x.destroy()
    
    def __edit(self):
        self.__save_btn['state'] = "normal"
        for x in self.__desFrm.winfo_children():
            x.destroy()
        dta = Selector.get().getData()
        self.__ent = Entry(self.__desFrm, width=25, font=(self._dFont['res'], self._dSize['res']))
        self.__ent.pack(anchor=W,pady=20, padx=5)
        self.__ent.insert(0, dta[0])
        Label(self.__desFrm, text="Progress "+ str(dta[1]) +"%", font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
        self.__desBx = Text(self.__desFrm, width=25, font=(self._dFont['res1'], self._dSize['res1']), height=5)
        self.__desBx.pack(anchor=W,pady=20, padx=5)
        self.__desBx.insert(END, dta[2])
        Label(self.__desFrm, text="Hash Code : " + str(dta[3]), font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
        
    def __p(self, i:int = 10):
        dt = Data()
        dt.increment(i, Selector.get())
        self.refresh()
    def __save(self):
        s = (self.__ent.get())
        d = (self.__desBx.get(1.0, "end-1c"))
        dt = Data()
        print(s, d)
        dt.EditName(s, Selector.get())
        dt.EditDes(d, Selector.get())
        self.__save_btn['state'] = 'disabled'
        self.refresh(op = 0)
    def __open(self):
        root = Tk()
        root.geometry("500x350")
    
        dta = Selector.get().getData()
        root.title(str(dta[0]))
        Label(root, text="Progress "+ str(dta[1]) +"%", font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
        Label(root, text= str(dta[2]), font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
        Label(root, text="Hash Code : " + str(dta[3]), font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)

        root.mainloop()
    
    def RoadMapWindow(self):
        self.__clrScr()
        self.__desFrm = LabelFrame(self.__rt)
        self.__desFrm.place(relx=0.01, rely=0.01, relheight=0.48, relwidth=0.38, anchor=NW)
        self.__toolFrm= LabelFrame(self.__rt)
        self.__toolFrm.place(relx=0.01, rely=0.98, relheight=0.48, relwidth=0.38, anchor=SW)
        self.__rdFrm = LabelFrame(self.__rt)
        self.__rdFrm.place(relx=0.98, rely=0.98, relheight=0.96, relwidth=0.58, anchor=SE)

        Button(self.__toolFrm, text="+1%", font=self._font['res'], width=20, command=lambda:self.__p(1)).pack(pady=10)
        Button(self.__toolFrm, text="+5%", font=self._font['res'], width=20, command=lambda:self.__p(5)).pack(pady=10)
        Button(self.__toolFrm, text="-5%", font=self._font['res'], width=20, command=lambda:self.__p(-5)).pack(pady=10)
        Button(self.__toolFrm, text="Edit", font=self._font['res'], width=20, command=self.__edit).pack(pady=10)
        self.__save_btn=Button(self.__toolFrm, text="Save", font=self._font['res'], width=20, command=self.__save)
        self.__save_btn.pack(pady=10)
        self.__save_btn['state'] = "disabled"
        Button(self.__toolFrm, text="Open", font=self._font['res'], width=20, command=self.__open).pack(pady=10)
        self.refresh(op = 0)

    def refresh(self, op:int = 1) -> None:
        if(op==1 or op ==0):  #Refresh Description
            for wid in self.__desFrm.winfo_children():
                wid.destroy()
            dta = Selector.get().getData()
            Label(self.__desFrm, text=str(dta[0]), font=(self._dFont['res'], self._dSize['res'])).pack(anchor=W,pady=20, padx=5)
            Label(self.__desFrm, text="Progress "+ str(dta[1]) +"%", font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
            Label(self.__desFrm, text= str(dta[2]), font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)
            Label(self.__desFrm, text="Hash Code : " + str(dta[3]), font=(self._dFont['res1'], self._dSize['res1']), fg=self._dColor['res1']).pack(anchor=W, pady=10, padx=10)

        if(op==2 or op == 0):
            for wid in self.__rdFrm.winfo_children():
                wid.destroy()
            Label(self.__rdFrm, text=u'\u2193', font=("Consolas", 25)).pack(pady=5)
            for btn in self.__obj:
                btn.create(self.__rdFrm).pack(pady=5)
                Label(self.__rdFrm, text=u'\u2193', font=("Consolas", 25)).pack(pady=5)

    def Select(self, obj:SubTask):
        self.__sel = obj
        
    def Enable(self):
        self.__rt.mainloop()

class Hash:
    __aph = string.ascii_lowercase
    __num = list(map(str, range(0,10)))
    __sym = "!@#$%^&*()"
    __code = ''
    
    def GenerateCode(self):
        dta = Data().getHash()
        self.__code = ''
        self.__code += ( random.choice(self.__aph) + random.choice(self.__aph) + random.choice(self.__aph) )
        self.__code += ( random.choice(self.__num) + random.choice(self.__num) )
        self.__code += random.choice(self.__sym)
        if self.__code in dta:
            self.GenerateCode()
        return self.__code    

class Window(Formate):
    __frm:Frame = None
    __title = None
    __disFrm = None
    __objs:list[RoadMap] = None
    __state = False
    __rt:Tk = None

    def __init__(self, objs:list[RoadMap]) -> None:
        self.__rt = Tk()
        self.__rt.geometry("1000x1000")
        self.__rt.title(self._Title)
        width = self.__rt.winfo_screenwidth() - 50
        height = self.__rt.winfo_screenheight() - 50
        self.__rt.geometry('%dx%d'%(width, height))
        self.__objs = objs
    
    def RoadMap(self):
        self.__disFrm = LabelFrame(self.__rt)
        self.__disFrm.place(relx=0.99, rely=0.01, anchor=NE, relheight=0.99, relwidth=0.4)
    
    def Enable(self):
        self.__rt.mainloop()


class Security:
    pass

class EncryptDta:
    __key = b'SzwHFgWh4A6xjZlBHHNCM0JkDaq2l8sBiLMX7Tq_MHc='
