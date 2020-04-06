from data_init import ori_data
from model import Status

memory = ori_data.memory()
process = ori_data.process()    
m = 0
p = 0
executing=[]
check = True

while(check):
    check = False

        

    #end
    for i in range(0, len(process)):
        if(process[i].time>0):
            check = True