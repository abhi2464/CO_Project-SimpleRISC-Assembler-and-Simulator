import re
rtype = {
    'opcode':'0110011',
    'funct3':{'add':'000','sub':'000', 'sll':'001', 'slt':'010', 'sltu':'011', 'xor':'100', 'srl':'101','or':'110','and':'111'},
    'funct7':{'add':'0000000','sub':'0100000', 'sll':'0000000', 'slt':'0000000', 'sltu':'0000000', 'xor':'0000000', 'srl':'0000000','or':'0000000','and':'0000000'}
}

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

registers = {
    "x0": {"address": "00000", "value": 0},
    "x1": {"address": "00001", "value": 0},
    "x2": {"address": "00010", "value": 0},
    "x3": {"address": "00011", "value": 0},
    "x4": {"address": "00100", "value": 0},
    "x5": {"address": "00101", "value": 0},
    "x6": {"address": "00110", "value": 0},
    "x7": {"address": "00111", "value": 0},
    "x8": {"address": "01000", "value": 0},
    "x9": {"address": "01001", "value": 0},
    "x10": {"address": "01010", "value": 0},
    "x11": {"address": "01011", "value": 0},
    "x12": {"address": "01100", "value": 0},
    "x13": {"address": "01101", "value": 0},
    "x14": {"address": "01110", "value": 0},
    "x15": {"address": "01111", "value": 0},
    "x16": {"address": "10000", "value": 0},
    "x17": {"address": "10001", "value": 0},
    "x18": {"address": "10010", "value": 0},
    "x19": {"address": "10011", "value": 0},
    "x20": {"address": "10100", "value": 0},
    "x21": {"address": "10101", "value": 0},
    "x22": {"address": "10110", "value": 0},
    "x23": {"address": "10111", "value": 0},
    "x24": {"address": "11000", "value": 0},
    "x25": {"address": "11001", "value": 0},
    "x26": {"address": "11010", "value": 0},
    "x27": {"address": "11011", "value": 0},
    "x28": {"address": "11100", "value": 0},
    "x29": {"address": "11101", "value": 0},
    "x30": {"address": "11110", "value": 0},
    "x31": {"address": "11111", "value": 0},
}


def getregisters(reg):
    try:
        return registers[reg]["address"]
    except:
        exit("Register Not Found")


with open('input.txt', 'r') as file:
    data = file.readlines()

with open("output.txt", 'w') as file:
    file.writelines("")
    
for x in data:
    temp=re.split(r"[, ]+",x)
    command = temp[0]
    if (command in rtype['funct3']):
        dest = getregisters(temp[1].strip())
        s1 = getregisters(temp[2].strip())
        s2 = getregisters(temp[3].strip())
        opcode = rtype['opcode']
        funct3 = rtype['funct3'][command]
        funct7 = rtype['funct7'][command]
        with open("output.txt", 'a') as file:
            f = f"{funct7}{s2}{s1}{funct3}{dest}{opcode}\n"
            file.writelines(f)
        
    elif command=='jal':
        opcode=jtype['opcode']
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(20)] ) )
        reg=getregisters(temp[1].strip())
        imm=bin(int(temp[2]))
        # print(imm[0],imm[len(imm)-10:len(imm)],imm[len(imm)-11],imm[len(imm)-19:len(imm)-11],reg,opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[0]}{imm[len(imm)-10:len(imm)]}{imm[len(imm)-11]}{imm[len(imm)-19:len(imm)-11]}{reg}{opcode}\n"
            file.writelines(f)
    
    elif (command in stype['funct3']):
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(12)] ) )
        opcode = stype['opcode']
        dest=getregisters(temp[1].strip())
        funct3 =stype['funct3'][command]
        imm=bin(int(temp[2]))
        s1 = getregisters(temp[3].strip())
        # print(imm[len(imm)-1-11:len(imm)-5],dest,s1,funct3,imm[len(imm)-1-4:len(imm)],opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[len(imm)-1-11:len(imm)-5]}{dest}{s1}{funct3}{imm[len(imm)-1-4:len(imm)]}{opcode}\n"
            file.writelines(f)

        
