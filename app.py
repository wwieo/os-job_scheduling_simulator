from data_init import ori_data
from operator import itemgetter, attrgetter

def add_rst(memory, process, para):
    rst =  (str(memory.mid)+"       "+
            str(process.size)+"      "+
            str(process.pid))
    if(process.pid<10):
        rst+=("       ")
    else:
        rst+=("      ")
    rst+=str(int(memory.size)-int(process.size))
    if((memory.size-process.size)>9):
        rst+= ("      "+process.status)
    else:
        rst+= ("       "+process.status)
    
    printRst = rst
    rst+="\n"
    
    with open('result.txt','a') as r:
        if(para):
            rst+="\n"
        r.write(rst)

    if(para):
        printRst+="\n"
    print(printRst)
    


with open('result.txt','a') as r:
    r.truncate(0)
    r.write("Memory  Use     Pid     Free    Status\n")
print("Memory  Use     Pid     Free    Status")

memory = ori_data.memory()
process = ori_data.process()    

check = True
systemClock = 0

p = 0
m = 0
executing_process = []

while(check):
    check = False
    for p in range(len(process)):  
        for m in range(len(memory)):
            if(memory[m].isUsing is False):
                if(process[p].isUsing is False):
                    if(memory[m].size >= process[p].size):
                        process[p].isUsing = True
                        memory[m].isUsing = True
                        process[p].memory = memory[m]
                        process[p].clockEnd += systemClock

                        clockStatus = []
                        for pp in range(len(executing_process)):
                            add_rst(executing_process[pp].memory, executing_process[pp], False)
                            
                        add_rst(process[p].memory, process[p], True)
                        executing_process.append(process[p])
                        break
   
    end = []
    for e in range(len(executing_process)):
        exe = executing_process[e]
        if(exe.clockEnd == systemClock):
            end.append(exe)
    end = sorted(end, key = attrgetter('memory.mid'))
    while(end):
        d = -1
        for ex in range(len(executing_process)):
            exe = executing_process[ex]
            if(exe == end[0]):
                exe.status = "End"
                process[exe.pid-1].status = "End"
                memory[exe.memory.mid-1].isUsing = False
                if(d<0):
                    d = ex
            else:
                add_rst(exe.memory, exe, False)
        if(d>=0):
            del executing_process[d]
        add_rst(end[0].memory, end[0], True)
        del end[0]
    
    for p in range(len(process)):  
        for m in range(len(memory)):
            if(memory[m].isUsing is False):
                if(process[p].isUsing is False):
                    if(memory[m].size >= process[p].size):
                        process[p].isUsing = True
                        memory[m].isUsing = True
                        process[p].memory = memory[m]
                        process[p].clockEnd += systemClock
                        clockStatus = []
                        for pp in range(len(executing_process)):
                            add_rst(executing_process[pp].memory, executing_process[pp], False)
          
                        add_rst(process[p].memory, process[p], True)
                        executing_process.append(process[p])
                        break

    systemClock += 1
    
    #end
    for i in range(0, len(process)):
        if(process[i].status == "Start"):
            check = True

