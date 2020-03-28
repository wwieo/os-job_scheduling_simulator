import json

class Process(object):
    def __init__(self, pid:int , size:int , time: int) -> None:
        self.pid = pid
        self.size = size
        self.time = time

class ori_data():
    def memory():
        with open('test_data.json' , 'r') as reader:
            ori_json = json.loads(reader.read())
        memory = ori_json["memory"]
        return memory

    def process():
        with open('test_data.json' , 'r') as reader:
            ori_json = json.loads(reader.read())
        process_ori = ori_json["process"]
        process_list = []

        for i in range(0, len(process_ori)):
            p = Process(pid=i+1, size=process_ori[i]["size"], time=process_ori[i]["time"])
            process_list.append(p)
        return process_list