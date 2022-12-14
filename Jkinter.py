from tkinter import *
import pyautogui as pyg
pyg
class Formate(object):
    _font = {1: "Consolas", 2:"Consolas"}
    _color= {1: "grey", 2:"black"}
    _size = {1: 15, 2: 15}

    _dFont= {1: "Consolas", 2:"Consolas"}
    _dColor= {1: "grey20", 2:"grey50"}
    _dSize = {1: 15, 2: 12}


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

    def __onClick(self):
        root = Tk()
        root.geometry("500x150")
        root.title(self.__name)
        lb1 = Label(root, text=self.__name, font=(self._dFont[self.__type], self._dSize[self.__type]), fg = self._dColor[self.__type])
        lb1.pack(anchor=W)

        lb2 = Label(root, text=self.__About, font=(self._dFont[2], self._dSize[2]), fg = self._dColor[2])
        lb2.pack(anchor=W)

        root.mainloop()

    def create(self, tk):
        self.__btn = Button(tk, text=self.__name, font=(self._font[self.__type], self._size[self.__type]))
        self.__btn['bg'] = self._color[self.__type]
        self.__btn['command'] = self.__onClick
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
        self.__btn = Button(tk, text=self.__name, font=(self._font[self.__type], self._size[self.__type]))
        self.__btn['text'] += (" "+str(self.__progress))
        return self.__btn

    def onClick(self):
        pass

