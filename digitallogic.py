import time

class Bin:
    def __init__(self, value):
        self.value = value
        self.size = len(value)

    def update_val(self,value):
        self.value = value

    def display(self):
        print(self.value)

    def binarytohex(self):
        fin_hex = ""
        work_bin = self.value
        if self.size%4 != 0:
            work_bin = "0"*(4-self.size%4) + work_bin
        for i in range(0,len(work_bin),4):
            cur_str = work_bin[i:i+4]
            hexint = 0
            for j in range(4):
                hexint+= int(cur_str[j])*(2**(3-j))
            hexstr = ""
            if hexint >= 10:
                hexstr = chr(55+hexint)
            else:
                hexstr = str(hexint)
            fin_hex += hexstr
        return fin_hex 

class Hex:
    def __init__(self, value):
        self.value = value
        self.size = len(value)
    
    def update_val(self,value):
        self.value = value

    def display(self):
        print (self.value)

    def hextobin(self):
        fin_binary = ""
        for i in self.value:
            if i.isdigit() == False:
                n = ord(i) - 55
            else:
                n = int(i)
            hexbits = ""
            while len(hexbits) < 4:
                hexbits += str(n%2)
                n = n//2
            fin_binary += hexbits[::-1]
        return fin_binary
    
class Flipflip:
    def __init__(self):
        self.data = 0
        self.Qout = 0
        self.prev_clk = 0

    def set_data(self,data):
        self.data = data

    def clock_in(self,clk):
        if self.prev_clk == 0 and clk == 1:
            self.Qout == self.data
        self.prev_clk = clk

def createbin(binval):
    for i in binval:
        if i not in ["0","1"]:
            print("Invalid Binary Value")
            return
    binout = Bin(binval)
    return binout

def createhex(hexval):
    for i in hexval:
        if i.isdigit() == False and (i < "A" or i > "F"):
            return
    hexout = Hex(hexval)
    return hexout

def size_comp(val1, val2):
    if isinstance(val1,Hex) or isinstance(val1,Bin):
        if val1.size != val2.size:
            return False
    else:
        if len(val1) != len(val2):
            return False

def bin_address_convert(bin):
    bit_list = []
    for i in bin:
        bit_list.append(i)
    return bit_list

def dectobin(dec, size = 8):
    if dec == 0:
            return "0"*size
    binout = ""
    binout_bits = []
    while dec > 0:
        r = dec % 2
        binout = str(r) + binout
        binout_bits.insert(0, str(r))
        dec = dec // 2
    if len(binout) > size:
        return -1
    if len(binout) < size:
        binout = "0"*(size-len(binout)) + binout
        fill = ["0"]*(size-len(binout_bits))
        binout_bits = fill.extend(binout_bits)
    return binout, binout_bits

def dectohex(dec, size = 2):
    if dec == 0:
        return "0"*size
    hex_chars = "0123456789ABCDEF"
    hexout = ""
    while dec > 0:
        r = dec % 16
        hexout = hex_chars[r] + hexout
        dec = dec // 16
    if len(hexout) < size:
        hexout = "0"*(size-len(hexout)) + hexout
    return hexout

def bin_and(bit1, bit2):
    bitout = ""
    if bit1 == bit2:
        bitout = bit1
    else:
        bitout = "0"
    return bitout

def bin_or(bit1, bit2):
    bitout = ""
    if bit1 == "1" or bit2 =="1":
        bitout = "1"
    else:
        bitout = "0"
    return bitout

def bin_xor(bit1, bit2):
    if bit1 == bit2:
        bitout = "0"
    else:
        bitout = "1"
    return bitout

def bin_and_n(*args):
    and_out = "1"
    for i in args:
        and_out = bin_and(and_out,i)
    return and_out

def bin_or_n(*args):
    or_out = "1"
    for i in args:
        or_out = bin_or(or_out,i)
    return or_out

def bin_xor_n(*args):
    xor_out = "1"
    for i in args:
        xor_out = bin_xor(xor_out,i)
    return xor_out

def binary_and(bin1, bin2):
    andout = ""
    binval1 = bin1.value
    binval2 = bin2.value
    if bin1.size != bin2.size:
        print("Unequal values")
        return
    no_bits = len(binval1)
    for i in range(no_bits):
        andout += bin_and(binval1[i], binval2[i])
    andoutbin = createbin(andout)
    return andoutbin

def binary_or(bin1, bin2):
    orout = ""
    binval1 = bin1.value
    binval2 = bin2.value
    if bin1.size != bin2.size:
        print("Unequal values")
        return
    no_bits = len(binval1)
    for i in range(no_bits):
        orout += bin_or(binval1[i], binval2[i])
    oroutbin = createbin(orout)
    return oroutbin

def binary_xor(bin1, bin2):
    xorout = ""
    binval1 = bin1.value
    binval2 = bin2.value
    if bin1.size != bin2.size:
        print("Unequal values")
        return
    no_bits = len(binval1)
    for i in range(no_bits):
        xorout += bin_xor(binval1[i], binval2[i])
    xoroutbin = createbin(xorout)
    return xoroutbin

def binary_and_n(*args):
    n = "1"*(len(args[0].value))
    and_out = createbin(n)
    for i in args:
        and_out = binary_and(and_out,i)
    return and_out

def bin_or_n(*args):
    or_out = "1"*(len(args[0].value))
    for i in args:
        or_out = binary_or(or_out,i)
    return or_out

def binary_xor_n(*args):
    xor_out = "1"*(len(args[0].value))
    for i in args:
        xor_out = binary_xor(xor_out,i)
    return xor_out

def hex_and(val1, val2):
    bin1 = createbin(val1.hextobin())
    andoutbin = binary_and(val1, val2)
    hexout = andoutbin.binarytohex()
    hexouthex = createhex(hexout)
    return hexouthex

def hex_or(val1, val2):
    oroutbin = binary_or(val1, val2)
    hexout = oroutbin.binarytohex()
    hexouthex = createhex(hexout)
    return hexouthex

def hex_xor(val1, val2):
    xoroutbin = binary_xor(val1, val2)
    hexout = xoroutbin.binarytohex()
    hexouthex = createhex(hexout)
    return hexouthex


def half_adder(a,b):
    s = bin_xor(a,b)
    c = bin_and(a,b)
    return s, c

def full_adder(a, b, c):
    s1 = bin_xor(a,b)
    sout = bin_xor(s1,c)
    c = bin_or(bin_and(a,b),bin_and(s1,c))
    return sout,c 
    
def nbit_add_sub(val1, val2, n = 8, k = 0):                                 #Add: k = 0
    if len(val1) > n or len(val2) > n:                              #Sub: k = 1
        print("Value greater than specified adder size")
        return
    if len(val1) < n:
        val1 = "0"*(n-len(val1)) + val1
    if len(val1) < n:
        val2 = "0"*(n-len(val2)) + val2
    sout = ""
    cout = ""
    c_n = str(k)
    ac = 0
    for i in range(n-1,-1,-1):
        a_n = val1[i]
        b_n = ""
        s_n = ""
        if k == 1:
            b_n = bin_xor(val2[i],str(k))
        else:
            b_n = val2[i]
        s_n, c_n = full_adder(a_n,b_n,c_n)
        if i == 4:
            ac = c_n
        sout = s_n + sout
    cout = c_n
    return sout, cout, ac

def mux2x1(a, b, s):
    if s:
        return b
    else:
        return a

def mux4x1(a,b,c,d,sline):
    s = sline.value
    if s == "00":
        return a
    elif s =="01":
        return b
    elif s == "10":
        return c
    elif s == "11":
        return d

def mux8x1(a,b,c,d,e,f,g,h,sline):
    s = sline.value
    if s == "000":
        return a
    elif s =="001":
        return b
    elif s == "010":
        return c
    elif s == "011":
        return d
    if s == "100":
        return e
    elif s =="101":
        return f
    elif s == "110":
        return g
    elif s == "111":
        return h
    


a = createhex("AB")
b = createhex("7E")
print(hex_and(a,b).value)
# for i in a.value:
#     if i == "1":
#         print("-",end="",flush=True)
#     else:
#         print("_",end="",flush=True)
#     time.sleep(0.7)








# val1 = createhex("A5")
# print(val1.value)
# print(val1.hextobin())
# print(val1.size)
# print()
# val2 = createhex("AA")
# print(val2.value)
# print(val2.hextobin())
# print(val2.size)
# print()
# val3 = hex_and(val1, val2)
# print("{} AND {} gives the result as {}".format(val1.value, val2.value, val3.value))

# val4 = hex_or(val1, val2)
# print("{} OR {} gives the result as {}".format(val1.value, val2.value, val4.value))

# val5 = hex_xor(val1, val2)
# print("{} XOR {} gives the result as {}".format(val1.value, val2.value, val5.value))