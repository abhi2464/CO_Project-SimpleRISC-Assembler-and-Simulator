import re
rtype = {
    'opcode':'0110011',
    'funct3':{'add':'000','sub':'000', 'sll':'001', 'slt':'010', 'sltu':'011', 'xor':'100', 'srl':'101','or':'110','and':'111'},
    'funct7':{'add':'0000000','sub':'0100000', 'sll':'0000000', 'slt':'0000000', 'sltu':'0000000', 'xor':'0000000', 'srl':'0000000','or':'0000000','and':'0000000'}
}

PC = 0 #Program Counter

jtype={
    'opcode':'1101111'
    
}

itype = {
    'opcode':{'lw':['0000011'],'addi':['0010011'],'sltiu':['0010011'],'jalr':['1100111']},
    'funct3' : {'lw':'010' , 'addi':'000' , 'sltiu':'011' , 'jalr':'000'}
}
itype_command = ['lw','addi','sltiu','jalr']

stype = {
    'opcode':'0100011',
    'funct3':{'sw':'010'}
}

utype ={
    'opcode':{'lui':'0110111','auipc':'0010111'},
    'funct3':{'lui','auipc'}
}

btype={
    'opcode':'1100011',
    'funct3':{'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}
}

#Register's Address
registers = {
    "zero": {"address": "00000", "value": ""},
    "ra": {"address": "00001", "value": ""},
    "sp": {"address": "00010", "value": ""},
    "gp": {"address": "00011", "value": ""},
    "tp": {"address": "00100", "value": ""},
    "t0": {"address": "00101", "value": ""},
    "t1": {"address": "00110", "value": ""},
    "t2": {"address": "00111", "value": ""},
    "s0": {"address": "01000", "value": ""},
    "fp": {"address": "01000", "value": ""},
    "s1": {"address": "01001", "value": ""},
    "a0": {"address": "01010", "value": ""},
    "a1": {"address": "01011", "value": ""},
    "a2": {"address": "01100", "value": ""},
    "a3": {"address": "01101", "value": ""},
    "a4": {"address": "01110", "value": ""},
    "a5": {"address": "01111", "value": ""},
    "a6": {"address": "10000", "value": ""},
    "a7": {"address": "10001", "value": ""},
    "s2": {"address": "10010", "value": ""},
    "s3": {"address": "10011", "value": ""},
    "s4": {"address": "10100", "value": ""},
    "s5": {"address": "10101", "value": ""},
    "s6": {"address": "10110", "value": ""},
    "s7": {"address": "10111", "value": ""},
    "s8": {"address": "11000", "value": ""},
    "s9": {"address": "11001", "value": ""},
    "s10": {"address": "11010", "value": ""},
    "s11": {"address": "11011", "value": ""},
    "t3": {"address": "11100", "value": ""},
    "t4": {"address": "11101", "value": ""},
    "t5": {"address": "11110", "value": ""},
    "t6": {"address": "11111", "value": ""},
}

# Register Check
def getregisters(reg):
    try:
        return registers[reg]
    except:
        exit(f"Register Not Found At Line No. {PC}")

# Immediate Value Check
def immediate_value(imm,x):
    if imm<((-2)**x) or imm>((2**x)-1):
        exit(f"Invalid Immediate Value At Line No. {PC}")
    else:
        bin = lambda imm : ''.join(reversed( [str((x >> i) & 1) for i in range(x)] ) )
        return bin(imm)

with open('input.txt', 'r') as file:
    data = file.readlines()

with open("output.txt", 'w') as file:
    file.writelines("")

#Removing empty lines from the program 
for i in data:
    if i=='\n':
        data.remove(i)

# Check for Virtual Halt   
if 'beq zero,zero,0' not in data:
    if 'beq zero,zero,0\n' not in data:
        exit('Virtual Halt Not Found In The Code')

# Main Program
for x in data:
    temp=re.split(r"[, ()\n]+",x)
    command = temp[0].strip()
    
    #R-Type Instructions
    if (command in rtype['funct3']):
        PC += 1
        dest = getregisters(temp[1].strip())["address"]
        s1 = getregisters(temp[2].strip())["address"]
        s2 = getregisters(temp[3].strip())["address"]
        opcode = rtype['opcode']
        funct3 = rtype['funct3'][command]
        funct7 = rtype['funct7'][command]
        with open("output.txt", 'a') as file:
            f = f"{funct7}{s2}{s1}{funct3}{dest}{opcode}\n"
            file.writelines(f)
    
    # J-Type Instructions   
    elif command=='jal':
        PC += 1
        opcode=jtype['opcode']
        reg=getregisters(temp[1].strip())["address"]
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(21)] ) )

        if int(temp[2])<(-2**21) or int(temp[2])>((2**21)-1):
            exit(f"Invalid Immediate Value At Line No. {PC}")
        else:
            imm=bin(int(temp[2]))

        # print(imm[0],imm[len(imm)-10-1:len(imm)-1],imm[len(imm)-1-11],imm[len(imm)-20:len(imm)-12],reg,opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[0]}{imm[len(imm)-10-1:len(imm)-1]}{imm[len(imm)-1-11]}{imm[len(imm)-20:len(imm)-12]}{reg}{opcode}\n"
            file.writelines(f)
    
    # S-Type Instructions
    elif (command in stype['funct3']):
        PC += 1
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(12)] ) )
        opcode = stype['opcode']
        dest=getregisters(temp[1].strip())["address"]
        funct3 =stype['funct3'][command]

        if int(temp[2])<(-2**12) or int(temp[2])>((2**12)-1):
            exit(f"Invalid Immediate Value At Line No. {PC}")
        else:
            imm=bin(int(temp[2]))

        s1 = getregisters(temp[3].strip())["address"]
        # print(imm[len(imm)-1-11:len(imm)-5],dest,s1,funct3,imm[len(imm)-1-4:len(imm)],opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[len(imm)-1-11:len(imm)-5]}{dest}{s1}{funct3}{imm[len(imm)-1-4:len(imm)]}{opcode}\n"
            file.writelines(f)

    # U-Type Instructions
    elif (command in utype['funct3']):
        PC+=1
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(32)] ) )
        opcode = utype['opcode'][command]
        dest= getregisters(temp[1].strip())['address']
        
        if (int(temp[2]))<(-2**32) or (int(temp[2]))>((2**32)-1):
            exit(f"Invalid Immediate Value At Line No. {PC}")
        else:
            imm=bin(int(temp[2]))

        # print(imm[0:len(imm)-12],dest,opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[0:len(imm)-12]}{dest}{opcode}\n"
            file.writelines(f)
    
    # I-Type Instructions
    elif command in itype_command:
        PC+=1
        opcode=itype['opcode'][command][0]
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(12)] ) )
        if command == 'lw':

            if int(temp[2])<(-2**12) or int(temp[2])>((2**12)-1):
                exit(f"Invalid Immediate Value At Line No. {PC}")
            else:
                imm=bin(int(temp[2]))

            s1 = getregisters(temp[1].strip())['address']
            s2 = getregisters(temp[3].strip())['address']
        else:

            if int(temp[3])<(-2**12) or int(temp[3])>((2**12)-1):
                exit(f"Invalid Immediate Value At Line No. {PC}")
            else:
                imm=bin(int(temp[3]))

            s1 = getregisters(temp[1].strip())['address']
            s2 = getregisters(temp[2].strip())['address']

        funct3 = itype['funct3'][command]
        # print(imm,s2,funct3,s1,opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm}{s2}{funct3}{s1}{opcode}\n"
            file.writelines(f)

    # B-Type Instructions
    elif command in btype["funct3"]:
        PC+=1
        opcode=btype['opcode']
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(16)] ) )

        if int(temp[3])<(-2**16) or int(temp[3])>((2**16)-1):
            exit(f"Invalid Immediate Value At Line No. {PC}")
        else:
            imm=bin(int(temp[3]))
        
        s1 = getregisters(temp[1].strip())['address']
        s2 = getregisters(temp[2].strip())['address']
        funct3 = btype['funct3'][command]
        # print(imm[len(imm)-1-12],imm[len(imm)-10-1:len(imm)-5],s2,s1,funct3,imm[len(imm)-5:len(imm)-1],imm[len(imm)-11-1],opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[len(imm)-1-12]}{imm[len(imm)-10-1:len(imm)-5]}{s2}{s1}{funct3}{imm[len(imm)-5:len(imm)-1]}{imm[len(imm)-11-1]}{opcode}\n"
            file.writelines(f)

    # Bonus Part
    elif command == "halt":
        PC += 1
        
        exit("Halted")
    

    elif command == "rvrs":
        PC += 1
        rs = getregisters(temp[2].strip())   
        rd = getregisters(temp[1].strip())
        rd["value"] = (rs["value"])[::-1]
        with open("output.txt", 'a') as file:
            f = f"0000000{rd['address']}000{rs['address']}000000000000\n"
            file.writelines(f)

        
    elif command == "rst":
        PC += 1
        for r in registers:
            registers[r]["value"] = ""


    elif command == "mul":
        PC += 1
        dest = getregisters(temp[1].strip())
        s1 = getregisters(temp[2].strip())
        s2 = getregisters(temp[3].strip())
        try:
            result = bin(int(s1["value"],2) * int(s2["value"],2))[2::]
            result = result[len(result)-32::]
            dest["value"] = result
        except:
            dest["value"] = "0"*32            
        with open("output.txt", 'a') as file:
            f = f"0000000{dest['address']}000{s1['address']}{s2['address']}0000000\n"
            file.writelines(f)
    else:
        exit("Instructions Not Found")        