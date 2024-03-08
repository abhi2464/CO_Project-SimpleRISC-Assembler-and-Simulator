import re
rtype = {
    'opcode':'0110011',
    'funct3':{'add':'000','sub':'000', 'sll':'001', 'slt':'010', 'sltu':'011', 'xor':'100', 'srl':'101','or':'110','and':'111'},
    'funct7':{'add':'0000000','sub':'0100000', 'sll':'0000000', 'slt':'0000000', 'sltu':'0000000', 'xor':'0000000', 'srl':'0000000','or':'0000000','and':'0000000'}
}
PC = 0
jtype={
    'opcode':'1101111'
    
}

itype = {
    'opcode':{'lw':['0000011'],'addi':['0010011'],'sltiu':['0010011'],'jalr':['1100011']},
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

registers = {
    "x0": {"address": "00000", "value": ""},
    "x1": {"address": "00001", "value": ""},
    "x2": {"address": "00010", "value": ""},
    "x3": {"address": "00011", "value": ""},
    "x4": {"address": "00100", "value": ""},
    "x5": {"address": "00101", "value": ""},
    "x6": {"address": "00110", "value": ""},
    "x7": {"address": "00111", "value": ""},
    "x8": {"address": "01000", "value": ""},
    "x9": {"address": "01001", "value": ""},
    "x10": {"address": "01010", "value": ""},
    "x11": {"address": "01011", "value": ""},
    "x12": {"address": "01100", "value": ""},
    "x13": {"address": "01101", "value": ""},
    "x14": {"address": "01110", "value": ""},
    "x15": {"address": "01111", "value": ""},
    "x16": {"address": "10000", "value": ""},
    "x17": {"address": "10001", "value": ""},
    "x18": {"address": "10010", "value": ""},
    "x19": {"address": "10011", "value": ""},
    "x20": {"address": "10100", "value": ""},
    "x21": {"address": "10101", "value": ""},
    "x22": {"address": "10110", "value": ""},
    "x23": {"address": "10111", "value": ""},
    "x24": {"address": "11000", "value": ""},
    "x25": {"address": "11001", "value": ""},
    "x26": {"address": "11010", "value": ""},
    "x27": {"address": "11011", "value": ""},
    "x28": {"address": "11100", "value": ""},
    "x29": {"address": "11101", "value": ""},
    "x30": {"address": "11110", "value": ""},
    "x31": {"address": "11111", "value": ""},
}


def getregisters(reg):
    try:
        return registers[reg]
    except:
        exit("Register Not Found")


with open('input.txt', 'r') as file:
    data = file.readlines()

with open("output.txt", 'w') as file:
    file.writelines("")

for x in data:

    temp=re.split(r"[, \n]+",x)
    command = temp[0].strip()
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
        
    elif command=='jal':
        PC += 1
        opcode=jtype['opcode']
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(20)] ) )
        reg=getregisters(temp[1].strip())["address"]
        imm=bin(int(temp[2]))
        # print(imm[0],imm[len(imm)-10:len(imm)],imm[len(imm)-11],imm[len(imm)-19:len(imm)-11],reg,opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[0]}{imm[len(imm)-10:len(imm)]}{imm[len(imm)-11]}{imm[len(imm)-19:len(imm)-11]}{reg}{opcode}\n"
            file.writelines(f)
    
    elif (command in stype['funct3']):
        PC += 1
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(12)] ) )
        opcode = stype['opcode']
        dest=getregisters(temp[1].strip())["address"]
        funct3 =stype['funct3'][command]
        imm=bin(int(temp[2]))
        s1 = getregisters(temp[3].strip())["address"]
        # print(imm[len(imm)-1-11:len(imm)-5],dest,s1,funct3,imm[len(imm)-1-4:len(imm)],opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[len(imm)-1-11:len(imm)-5]}{dest}{s1}{funct3}{imm[len(imm)-1-4:len(imm)]}{opcode}\n"
            file.writelines(f)

    elif (command in utype['funct3']):
        print(temp)
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(32)] ) )
        opcode = utype['opcode'][command]
        dest= getregisters(temp[1].strip())['address']
        imm= bin(int(temp[2]))
        # print(imm[0:len(imm)-12],dest,opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[0:len(imm)-12]}{dest}{opcode}\n"
            file.writelines(f)
    
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