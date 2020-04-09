
class Memory(object):
    def __init__(self, mid:int, size:int, isUsing:bool) -> None:
        self.mid = mid
        self.size = size
        self.isUsing = isUsing

class Process(object):
    def __init__(self, pid:int, size:int, isUsing:bool,
                 clockEnd:int, status:str, memory:object) -> None:
        self.pid = pid
        self.size = size
        self.isUsing = isUsing
        self.clockEnd = clockEnd
        self.status = status
        self.memory = memory
