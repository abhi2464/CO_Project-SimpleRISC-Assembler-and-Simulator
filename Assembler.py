import re
rtype = {
    'opcode':'0110011',
    'funct3':{'add':'000','sub':'000', 'sll':'001', 'slt':'010', 'sltu':'011', 'xor':'100', 'srl':'101','or':'110','and':'111'},
    'funct7':{'add':'0000000','sub':'0100000', 'sll':'0000000', 'slt':'0000000', 'sltu':'0000000', 'xor':'0000000', 'srl':'0000000','or':'0000000','and':'0000000'}
}

jtype={
    'opcode':'1101111'
    
}
register = {
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

with open('input.txt', 'r') as file:
    data = file.readlines()

with open("output.txt", 'w') as file:
    file.writelines("")
    
for x in data:
    command = x.split(",")[0].split(" ")[0].strip()
    dest = x.split(",")[0].split(" ")[1].strip()
    s1 = x.split(",")[1].strip()
    s2 = x.split(",")[2].strip()
    if (command in rtype['funct3']):
        opcode = rtype['opcode']
        destbin = register[dest]['address']
        funct3 = rtype['funct3'][command]
        s1bin = register[s1]['address']
        s2bin = register[s2]['address']
        funct7 = rtype['funct7'][command]
        print(opcode,destbin,funct3,s1bin,s2bin,funct7)
    
    if command=='jal':
        opcode=jtype['opcode']
        temp=re.split(r"[, ]+",x)
        bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(20)] ) )
        reg=register[temp[1]]['address']
        imm=bin(int(temp[2]))
        print(imm[19]+imm[9:0:-1]+imm[10]+imm[18:11:-1]+reg+opcode)
        with open("output.txt", 'a') as file:
            f = f"{imm[19]}{imm[9:0:-1]}{imm[10]}{imm[18:11:-1]}{reg}{opcode}\n"
            file.writelines(f)
        
    with open("output.txt", 'a') as file:
        #Aaman please reverse this encoding as it is mentioned in the table that 
        #we have to write the opcode at the least significant bit
        f = f"{opcode}{destbin}{funct3}{s1bin}{s2bin}{funct7}\n"
        file.writelines(f)
        
