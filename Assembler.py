rtype = {
    'opcode':['0110011'],
    'funct3':{'add':'000','sub':'000', 'sll':'001', 'slt':'010', 'sltu':'011', 'xor':'100', 'srl':'101','or':'110','and':'111'},
    'funct7':{'add':'0000000','sub':'0100000', 'sll':'0000000', 'slt':'0000000', 'sltu':'0000000', 'xor':'0000000', 'srl':'0000000','or':'0000000','and':'0000000'}
}

register = {
    'rs1':'00000',
    'rs2':'00001',
    'rs3':'00010',
    'rs4':'00011',
    'rd':'00100',
}

with open('input.txt', 'r') as file:
    data = file.readlines()
for x in data:
    command = x.split(",")[0].split(" ")[0].strip()
    dest = x.split(",")[0].split(" ")[1].strip()
    s1 = x.split(",")[1].strip()
    s2 = x.split(",")[2].strip()
    if (command in rtype['funct3']):
        opcode = rtype['opcode'][0]
        destbin = register[dest]
        funct3 = rtype['funct3'][command]
        s1bin = register[s1]
        s2bin = register[s2]
        funct7 = rtype['funct7'][command]
    print(opcode,destbin,funct3,s1bin,s2bin,funct7)
with open("output.txt", 'w') as file:
    f = f"{opcode} {destbin} {funct3} {s1bin} {s2bin} {funct7}"
    file.writelines(f)