from tkinter import *
import pyautogui as pyg
pyg
class Formate(object):
    _font = {1: "Consolas"}
    _color= {1: "grey"}
    _size = {1: 15}

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
    def onClick():
        pass
    def create(self, tk):
        self.__btn = Button(tk, text=self.__name, font=(self._font[self.__type], self._size[self.__type]))
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
    def __init__(self, task:list[SubTask], name:str) -> None:
        self.__subtask = task
        self.__name = name
        sum = 0
        for x in self.__subtask:
            self.__sum += x.progress
        self.__progress = self.sum // len(self.__subtask)
    def create(self, tk):
        self.btn = Button(tk, text=self.__name, font=(self._font[self.__type], self._size[self.__type]))
        return self.__btn
        