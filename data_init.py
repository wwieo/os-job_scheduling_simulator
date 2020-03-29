import json
from model import Process, Memory


class ori_data():
    def memory():
        with open('test_data.json' , 'r') as reader:
            ori_json = json.loads(reader.read())
        memory_ori = ori_json["memory"]
        memory_list = []

        for i in range(0, len(memory_ori)):
            m = Memory(mid=i+1, size=memory_ori[i], isUsing=False)
            memory_list.append(m)
        return memory_list

    def process():
        with open('test_data.json' , 'r') as reader:
            ori_json = json.loads(reader.read())
        process_ori = ori_json["process"]
        process_list = []

        for i in range(0, len(process_ori)):
            p = Process(pid=i+1, size=process_ori[i]["size"],
                        time=process_ori[i]["time"], finish=False)
            process_list.append(p)
        return process_list