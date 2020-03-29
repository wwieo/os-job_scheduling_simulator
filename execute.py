from data_init import ori_data

def add_rst(rst, memory, process):
    rst += (str(memory.mid)+"       "+
            str(process.size)+"      "+
            str(process.pid)+"       "+
            str(int(memory.size)-int(process.size))+"      Start\n")
    print(rst)
    
print("Memory  Use     Pid     Free    Status")

memory = ori_data.memory()
process = ori_data.process()

pcs_handled = []
executing = []
n = 0
i = 0
rst=""

while process[len(process)-1].finish is False:
    while i != len(memory)-1:
        if(memory[i].isUsing is False):
            if(memory[i].size>process[n].size):
                executing.append(process[n])
                memory[i].isUsing = True
                add_rst(rst, memory[i], process[n])
                i+=1
                n+=1
            else:
                pcs_handled.append(process[n].size)
                i+=1
        else:
            i+=1
            


    process[len(process)-1].executed = True
