from digitallogic import dectobin, Hex, Bin, nbit_add_sub
from memory_code import main_memory
from mem_def import *

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
def fetch_spc_reg_value(reg):
    reg_value = main_memory.load_data(reg)
    return reg_value

def imm_add_fetch(instr):
    operand2 = instr[1].lstrip()
    optype_identifier = operand2[0]
    if optype_identifier.isdigit() :         #COM X, YZh
        op2 = "0101"
        immediate_hex = Hex(operand2[:-1])
        immediate = immediate_hex.hextobin()
    elif operand2 in SpcRegDef.keys():      #COM X, PX
        op2 = "0101"
        regadd = SpcRegDef[operand2]
        print(operand2, regadd) 
        immediate_hex = Hex(regadd)
        immediate = immediate_hex.hextobin()
    elif optype_identifier == "R":          #COM X, Rn
        op2 = "1"
        rval = dectobin(int(operand2[1]),3)
        op2 = op2 + rval[0]
    elif optype_identifier == "#":          #COM X, #imm
        op2 = "0100"
        immediate_hex = Hex(operand2[1:-1])
        immediate = immediate_hex.hextobin()
    return op2, immediate
    
def imm_gen(instr):
    operand, immediate = imm_add_fetch(instr)
    if operand[0] == "1":                   #xxxx1nnn   nnn -> Rn [n: 0-7]
        address = ("0"*5) + operand[1:]
        address_bin = Bin(address)
        address_hex = address_bin.binarytohex()
        return main_memory.load_data(address_hex)
    elif operand == "0101":                 #direct address
        if immediate[0].isdigit():
            address_bin = immediate
            address_hex = address_bin.binarytohex()
            return main_memory.load_data(address_hex)
        else:
            address = SpcRegDef[immediate]      #Spc Reg call
            return fetch_spc_reg_value(address)
    else:
        return immediate


# MAIN
opcode = ""
immediate = ""
instr = input()
instr_list = instr.split(",")
operation = instr_list[0]
operation_type_list = {"ADD A":"0010", "MOV A":"1110", 'MOV R': "0111"}
main_memory.store_data("00001010",ACC)
op1 = operation_type_list[operation]

print(operation)

if op1 == "0010":   #ADD
    operand_value = imm_gen(instr_list)
    acc_value = fetch_spc_reg_value(ACC)
    add_result,cflgval, acflgval = nbit_add_sub(operand_value, acc_value)
    main_memory.store_data(add_result,ACC)

elif op1 == "1110": #MOV to A
    fetch_value = imm_gen(instr_list)  
    acc_value = fetch_spc_reg_value(ACC)
    main_memory.store_data(fetch_value,ACC)

elif op1

print(main_memory.load_data(ACC))
