from data_init import ori_data
from model import Status

def add_rst(memory, process):
    rst =  (str(memory.mid)+"       "+
            str(process.size)+"      "+
            str(process.pid)+"       "+
            str(int(memory.size)-int(process.size)))
    if((memory.size-process.size)>9):
        rst+= ("      "+process.finish)
    else:
        rst+= ("       "+process.finish)
    print(rst)
    
print("Memory  Use     Pid     Free    Status")

memory = ori_data.memory()
process = ori_data.process()    

pcs_handled = []
executing = []
m = 0
p = 0

while process[len(process)-1].finish == "Start":
    while p != len(process)-1:
        switch = False
        if(memory[m].isUsing is False):
            #pcs_handled
            if(memory[m].size>=process[p].size):
                executing.append(Status(memory=memory[m], process=process[p]))
                memory[m].isUsing = True
                m+=1
                p+=1
                for execute in executing:   
                    add_rst(execute.memory, execute.process)
                print("")
            else:
                need_be_handled = True
                for i in range(m, len(memory)):
                    if(memory[i].isUsing is False):
                        if(memory[i].size >= process[p].size):
                            executing.append(Status(memory=memory[i], process=process[p]))
                            memory[i].isUsing = True
                            need_be_handled = False
                            break
                if(need_be_handled):
                    pcs_handled.append(process[p])

                for execute in executing:   
                    add_rst(execute.memory, execute.process)    
                print("")
                p+=1
        else:
            m+=1

        for s in range(0, len(memory)):
            if(memory[s].isUsing is False):
                switch  = True

        if(switch is False):
            end = []
            for execute in executing:  
                execute.process.time -= 1
                if(execute.process.time == 0):
                    execute.memory.isUsing = False
                    end.append(execute)
            while(end):
                for i in range(0, len(executing)-1): 
                    if(executing[i].process.time == 0):
                        del executing[i]
                    add_rst(executing[i].memory, executing[i].process)
                end[0].process.finish = "End"
                add_rst(end[0].memory, end[0].process)
                print("")
                memory[(end[0].memory.mid)-1].isUsing = False
                process[(end[0].process.pid)-1].finish = "End"
                del end[0]
            m = 0   
