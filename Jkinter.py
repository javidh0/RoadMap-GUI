class RoadMap(object):
    _event = ""
    _overal_progress = 0
    _type = 0
    def __init__(self, a:str, b:int, c:int = 0) -> None:
        self._event = a
        self._progress = b
        self._type = c
    def get(self):
        pass

class SubTask:
    __name = None
    __About = None
    __progress = None
    __type = None
    def __init__(self, title:str = "Unknown Task", Note:str = "", progress:int = 0) -> None:
        self.__name = title
        self.__About = Note
        self.__progress = progress
    def onClick():
        pass
    def create():
        pass
    def edit():
        pass
    def save_in_file():
        pass
