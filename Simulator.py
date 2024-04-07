register_val={
    "00000":"00000000000000000000000000000000",
    "00001":"00000000000000000000000000000000",
    "00010":"00000000000000000000000100000000",
    "00011":"00000000000000000000000000000000",
    "00100":"00000000000000000000000000000000",
    "00101":"11111111111111111111111111111111",
    "00110":"00000000000000000000000000000011",
    "00111":"00000000000000000000000000000011",
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

data_mem={
    "65536":"00000000000000000000000000000000",
    "65540":"00000000000000000000000000000000",
    "65544":"00000000000000000000000000000000",
    "65548":"00000000000000000000000000000000",
    "65552":"00000000000000000000000000000000",
    "65556":"00000000000000000000000000000000",
    "65560":"00000000000000000000000000000000",
    "65564":"00000000000000000000000000000000",
    "65568":"00000000000000000000000000000000",
    "65572":"00000000000000000000000000000000",
    "65576":"00000000000000000000000000000000",
    "65580":"00000000000000000000000000000000",
    "65584":"00000000000000000000000000000000",
    "65588":"00000000000000000000000000000000",
    "65592":"00000000000000000000000000000000",
    "65596":"00000000000000000000000000000000",
    "65600":"00000000000000000000000000000000",
    "65604":"00000000000000000000000000000000",
    "65608":"00000000000000000000000000000000",
    "65612":"00000000000000000000000000000000",
    "65616":"00000000000000000000000000000000",
    "65620":"00000000000000000000000000000000",
    "65624":"00000000000000000000000000000000",
    "65628":"00000000000000000000000000000000",
    "65632":"00000000000000000000000000000000",
    "65636":"00000000000000000000000000000000",
    "65640":"00000000000000000000000000000000",
    "65644":"00000000000000000000000000000000",
    "65648":"00000000000000000000000000000000",
    "65652":"00000000000000000000000000000000",
    "65656":"00000000000000000000000000000000",
    "65660":"00000000000000000000000000000000"
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

ins_length=len(data) #Total No. Instructions

#Writing in Ouput File
def op_write():
    global PC
    global register_val
    with open("output.txt", 'a') as file:
        d=str("0b")
        bini = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(32)] ) )
        file.write(d+bini(PC))
        file.write(" ")
        for i in register_val:
            file.write(d+register_val[i])
            file.write(" ")
        file.write("\n")

#Writing the Data Memory
def memo_write():
    global data_mem
    with open("output.txt", 'a') as file:
        a=str(":")
        c="000"
        d=str("0b")
        for j in data_mem:
            b=hex(int(j))
            f=f"{b[0:2]}{c}{b[2:]}{a}{d+data_mem[j]}\n"
            file.writelines(f)
    exit()
    
#To Convert a Binary number to decimal
def deci(x, bits):
    assert len(x) <= bits
    n = int(x, 2)
    s = 1 << (bits - 1)
    return (n & s - 1) - (n & s)

PC=0 #Program Counter

#R-Type
def r_type(x):
    global PC
    bini = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(32)] ) )
    func=x[17:20]
    rd=x[20:25]
    rs1=x[12:17]
    rs2=x[7:12]
    if func=="000":
        #add
        PC+=4
        ans=deci(register_val[rs1],32)+deci(register_val[rs2],32)
        register_val[rd]=bini(ans)
        op_write()

    elif  func=="000" and x[0:7]=="0100000":
        #sub
        PC+=4
        ans=deci(register_val[rs1],32)-deci(register_val[rs2],32)
        register_val[rd]=bini(ans)
        op_write()

    elif func=="001":
        #sll
        PC+=4
        ans=deci(register_val[rs1],32)<<int(register_val[rs2][27:32],2)
        register_val[rd]=bini(ans)
        op_write()

    elif func=="010":
        #slt
        if deci(register_val[rs1],32)<deci(register_val(rs2),32):
            PC+=4
            register_val[rd]=bini(1)
            op_write()

    elif func=="011":
        #sltu
        if int(register_val[rs1],2)<int(register_val(rs2),2):
            PC+=4
            register_val[rd]=bini(1)
            op_write()
    
    elif func=="100":
        #xor
        PC+=4
        ans=deci(register_val[rs1],32)^deci(register_val[rs2],32)
        register_val[rd]=bini(ans)
        op_write()

    elif func=="101":
        #srl
        PC+=4
        ans=deci(register_val[rs1],32)>>int(register_val[rs2][27:32],2)
        register_val[rd]=bini(ans)
        op_write()

    elif func=="110":
        #or
        PC+=4
        ans=deci(register_val[rs1],32)|deci(register_val[rs2],32)
        register_val[rd]=bini(ans)
        op_write()
    
    elif func=="111":
        #and
        PC+=4
        ans=deci(register_val[rs1],32)&deci(register_val[rs2],32)
        register_val[rd]=bini(ans)
        op_write()

#J-Type
def j_type(x):
    global PC
    bini = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(32)] ) )
    rd=x[20:25]
    imm=x[0]+x[12:20]+x[11]+x[1:11]+"0"
    imm_dec=deci(imm,len(imm))
    register_val[rd]=bini(PC+4)
    PC=PC+imm_dec
    execute(PC//4)

def b_type(x):
    global PC
    bini = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(32)] ) )
    func=x[17:20]
    rs1=x[12:17]
    rs2=x[7:12]
    imm=x[0]+x[24]+x[1:7]+x[20:24]+"0"
    imm_dec=deci(imm,len(imm))

    if func=="000" and deci(register_val[rs1],32)==deci(register_val[rs2],32): #beq
        PC=PC+imm_dec
        execute(PC//4)

    elif func=="001" and deci(register_val[rs1],32)!=deci(register_val[rs2],32): #bne
        PC=PC+imm_dec
        execute(PC//4)

    elif func=="100" and deci(register_val[rs1],32)<deci(register_val[rs2],32): #blt
        PC=PC+imm_dec
        execute(PC//4)

    elif func=="101" and deci(register_val[rs1],32)>=deci(register_val[rs2],32): #bge
        PC=PC+imm_dec
        execute(PC//4)

    elif func=="110" and int(register_val[rs1],2)<int(register_val[rs2],2): #bltu
        PC=PC+imm_dec
        execute(PC//4)

    elif func=="111" and deci(register_val[rs1],32)>=deci(register_val[rs2],32): #begu
        PC=PC+imm_dec
        execute(PC//4)


def u_type(x,opcode):
    rd = x[20:25]
    print(PC)    
    if opcode == '0010111':
        imm = bin((int(x[0:20],2) << 12) + PC)
        register_val[rd] = imm
        op_write()
    elif opcode == '0110111':
        imm = bin((int(x[0:20],2) << 12))
        register_val[rd] = imm
        op_write()


# print(data)
def execute(start):
    global PC
    # global ins_length
    for x in range(start,ins_length):

        if data[x]=="00000000000000000000000001100011": #Virtual Halt
            PC+=4
            op_write()
            memo_write()
        
        elif data[x][25:len(data[x])]=="0110011": #R-Type
            r_type(data[x])
        
        elif data[x][25:len(data[x])]=="1101111": #J-Type
            j_type(data[x])

        elif data[x][25:len(data[x])]=="1100011": #B-Type
            b_type(data[x])

        elif data[x][25:len(data[x])]=="0110111": #U-Type
            u_type(data[x],'0110111')
        
        elif data[x][25:len(data[x])]=="0010111": #U-Type
            u_type(data[x],'0010111')
            
        


execute(0)
# print (register_val)
