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
        if(m <= len(memory)):
            if(memory[m].isUsing is False):
                if(memory[m].size>=process[p].size):
                    executing.append(Status(memory=memory[m], process=process[p]))
                    memory[m].isUsing = True
                    m+=1
                    p+=1
                else:
                    for i in range(m, len(memory)):
                        if(memory[i].size >= process[p].size):
                            executing.append(Status(memory=memory[i], process=process[p]))
                            memory[i].isUsing = True
                            break
                    p+=1
            else:
                m+=1
                
        switch = False
        for s in range(0, len(memory)):
            if(memory[s].isUsing is False):
                switch  = True
            
        if(switch):
            for execute in executing:   
                add_rst(execute.memory, execute.process)
            print("")
        else:
            end = []
            for execute in executing:  
                execute.process.time -= 1
                if(execute.process.time == 0):
                    execute.memory.isUsing = False
                    end.append(execute)
            #print("len",len(end))
            while(end):
                for i in range(0, len(executing)-1):   
                    add_rst(executing[i].memory, executing[i].process)
                    if(executing[i].process.time == 0):
                        del executing[i]
                end[0].process.finish = "End"
                add_rst(end[0].memory, end[0].process)
                print("")
                del end[0]
            m = 0   
            
        

    process[len(process)-1].finish = "End"
