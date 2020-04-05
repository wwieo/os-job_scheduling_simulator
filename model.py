
class Memory(object):
    def __init__(self, mid:int, size:int, isUsing:bool) -> None:
        self.mid = mid
        self.size = size
        self.isUsing = isUsing

class Process(object):
    def __init__(self, pid:int, size:int, 
                 time: int, finish: str) -> None:
        self.pid = pid
        self.size = size
        self.time = time
        self.finish = finish

class Status(object):
    def __init__(self, memory:object, process:object) -> None:
        self.memory = memory
        self.process = process
