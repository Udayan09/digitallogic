from typing import Any
from digitallogic import dectohex, bin_address_convert

class Memory:
    def __init__(self, ref):
        self.regs = {}
        self.sp = 0
        self.size = 128

    def add_register(self, register):
        register.add = dectohex(self.sp)
        self.regs[register.add] = register
        self.sp += 1
    
    def store_data(self, data, address):
        bin_data = data
        bin_data_bits = bin_address_convert(data) 
        if isinstance(self.regs[address],Register):
            if bin_data == -1:
                bin_data = "0"*8
            self.regs[address].data = bin_data
        else:
            if bin_data == -1:
                bin_data_bits = ["0"]*8
            self.regs[address].data = bin_data_bits
        

    def load_data(self, address):
        return self.regs[address].data

    def clear_data(self, address):
        self.regs[address].data = "0"*8

class Register:
    def __init__(self, ref):
        self.size = 8
        self.data = "0"*8
        self.add = 0
        self.ref = ref

    def byte(self):
        return self.data
    
class Bit_address_register:
    def __init__(self, ref):
        self.size = 8
        self.data = ["0"]*8
        self.add = 0
        self.ref = ref

    def update_val(self, data, index):
        new_index = 7 - index
        self.data[new_index] = data

    def byte(self):
        byteout = ""
        for i in self.data:
            byteout += i
        return byteout

main_memory = Memory("mem1")

for i in range(128):
    obj = Register(f"M{i}")
    main_memory.add_register(obj)
