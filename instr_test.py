import digitallogic
from memory_code import main_memory
import mem_gui

acc = "00001011"

sfr = dict()
sfr_spec = ["C","AC","F0","RS1","RS0","OV","","P"]
for i in sfr_spec:
    sfr[i] = "0"

opcodes = {"AND":1,"SUB":2,"INC":3}


#Testing Assembly addition.
code_line = list(input().split())


intermediate = code_line[1][:-1]

inter_value = main_memory.load_data(intermediate)

acc, sfr["C"], sfr["AC"] = digitallogic.nbit_add_sub(acc, inter_value, n = 8)

main_memory.store_data(acc,"1F")
print(sfr.values())
mem_gui.create_tree()


