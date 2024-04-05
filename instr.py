from digitallogic import dectobin, Hex, Bin
from memory_code import main_memory

'''
Immediate Addressing:
ADD A, #10H

Register Addressing:
ADD A, R0-R7

Direct Addressing:
ADD A,30H    ---> Memory Space in the RAM
                  30H ---> [#10]

Register Indirect Addressing:
ADD A, @R0 or @R1 or @DPTR(16bit)

'''

'''
MOV X, Y
Logic: LOAD data from address location Y and STORE it into address location X

'''

def decoder(opcode, immediate):
    operation = opcode[0:4]
    operand = opcode[4:]
    if operand[0] == "1":
        address = ("0"*5) + operand[1:]
        return main_memory.load_data(address)
    elif operand == "0101":
        address = immediate
        return main_memory.load_data(address)
    elif operand[:-1] == "011":
        address = ("0"*7) + operand[-1]
    else:
        return immediate

opcode = ""
immediate = ""
instr = input()
pre_opcode = instr.split(",")
operation = pre_opcode[0].split()[0]
operation_type_list = {"ADD":"0001", "MOV":"0010"}
op1 = operation_type_list[operation]
if op1 == "0001":
    operand = pre_opcode[1].lstrip()
    optype_identifier = operand[0]
    if optype_identifier.isdigit():
        op2 = "0101"
    elif optype_identifier == "R":
        op2 = "1"
        rval = dectobin(int(operand[1]),3)
        op2 = op2 + rval[0]
    elif optype_identifier == "#":
        op2 = "0100"
        immediate_hex = Hex(operand[1:-1])
        immediate = immediate_hex.hextobin()
    else:
        op2 = "0101"
        immediate_hex = Hex(operand[:-1])
        immediate = immediate_hex.hextobin()
    opcode = op1 + op2
elif op1 == "0010":
    pass


acc_val = main_memory.load_data(64)
