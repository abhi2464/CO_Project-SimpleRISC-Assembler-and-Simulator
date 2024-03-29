register_add={
    "00000":"00000000000000000000000000000000",
    "00001":"00000000000000000000000000000010",
    "00010":"00000000000000000000000000000011",
    "00011":"00000000000000000000000000000000",
    "00100":"00000000000000000000000000000000",
    "00101":"00000000000000000000000000000000",
    "00110":"00000000000000000000000000000000",
    "00111":"00000000000000000000000000000000",
    "01000":"00000000000000000000000000000000",
    "01001":"00000000000000000000000000000000",
    "01010":"00000000000000000000000000000000",
    "01011":"00000000000000000000000000000000",
    "01100":"00000000000000000000000000000000",
    "01101":"00000000000000000000000000000000",
    "01110":"00000000000000000000000000000000",
    "01111":"00000000000000000000000000000000",
    "10000":"00000000000000000000000000000000",
    "10001":"00000000000000000000000000000000",
    "10010":"00000000000000000000000000000000",
    "10011":"00000000000000000000000000000000",
    "10100":"00000000000000000000000000000000",
    "10101":"00000000000000000000000000000000",
    "10110":"00000000000000000000000000000000",
    "10111":"00000000000000000000000000000000",
    "11000":"00000000000000000000000000000000",
    "11001":"00000000000000000000000000000000",
    "11010":"00000000000000000000000000000000",
    "11011":"00000000000000000000000000000000",
    "11100":"00000000000000000000000000000000",
    "11101":"00000000000000000000000000000000",
    "11110":"00000000000000000000000000000000",
    "11111":"00000000000000000000000000000000"
}

with open("input.txt", 'r') as file:
    data = file.readlines()

with open("output.txt", 'w') as file:
    file.writelines("")

for j in range(len(data)):
    if data[j].strip()=='\n':
        pass
    else:
        data[j]=data[j].strip()

#To Convert a Binary number to decimal
def deci(x, bits):
    assert len(x) <= bits
    n = int(x, 2)
    s = 1 << (bits - 1)
    return (n & s - 1) - (n & s)

PC=-4 #Program Counter
def r_type(x):
    bini = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(32)] ) )
    func=x[17:20]
    rd=x[20:25]
    rs1=x[12:17]
    rs2=x[7:12]
    if func=="000":
        #add
        ans=deci(register_add[rs1],32)+deci(register_add[rs2],32)
        register_add[rd]=bini(ans)

    elif  func=="000" and x[0:7]=="0100000":
        #sub
        ans=deci(register_add[rs1],32)-deci(register_add[rs2],32)
        register_add[rd]=bini(ans)

    elif func=="001":
        #sll
        ans=deci(register_add(rs1),32)<<int(register_add[rs2][27:32],2)
        register_add[rd]=bini(ans)

    elif func=="010":
        #slt
        if deci(register_add(rs1),32)<deci(register_add(rs2),32):
            register_add[rd]=bini(1)

    elif func=="011":
        #sltu
        if int(register_add(rs1),2)<int(register_add(rs2),2):
            register_add[rd]=bini(1)
    
    elif func=="100":
        #xor
        ans=deci(register_add[rs1],32)^deci(register_add[rs2],32)
        register_add[rd]=bini(ans)

    elif func=="101":
        #srl
        ans=deci(register_add(rs1),32)>>int(register_add[rs2][27:32],2)
        register_add[rd]=bini(ans)

    elif func=="110":
        #or
        ans=deci(register_add[rs1],32)|deci(register_add[rs2],32)
        register_add[rd]=bini(ans)
    
    elif func=="111":
        #and
        ans=deci(register_add[rs1],32)&deci(register_add[rs2],32)
        register_add[rd]=bini(ans)

# print(data)
for x in data:
    if x[25:len(x)]=="0110011":
        PC+=4
        r_type(x)
print (register_add)