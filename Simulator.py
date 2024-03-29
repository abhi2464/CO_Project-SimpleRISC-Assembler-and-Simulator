register_add={
    "00000":"00000000000000000000000000000000",
    "00001":"00000000000000000000000000000000",
    "00010":"00000000000000000000000000000000",
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
# registers = {
#     "zero": {"address": "00000", "value": ""},
#     "ra": {"address": "00001", "value": ""},
#     "sp": {"address": "00010", "value": ""},
#     "gp": {"address": "00011", "value": ""},
#     "tp": {"address": "00100", "value": ""},
#     "t0": {"address": "00101", "value": ""},
#     "t1": {"address": "00110", "value": ""},
#     "t2": {"address": "00111", "value": ""},
#     "s0": {"address": "01000", "value": ""},
#     "fp": {"address": "01000", "value": ""},
#     "s1": {"address": "01001", "value": ""},
#     "a0": {"address": "01010", "value": ""},
#     "a1": {"address": "01011", "value": ""},
#     "a2": {"address": "01100", "value": ""},
#     "a3": {"address": "01101", "value": ""},
#     "a4": {"address": "01110", "value": ""},
#     "a5": {"address": "01111", "value": ""},
#     "a6": {"address": "10000", "value": ""},
#     "a7": {"address": "10001", "value": ""},
#     "s2": {"address": "10010", "value": ""},
#     "s3": {"address": "10011", "value": ""},
#     "s4": {"address": "10100", "value": ""},
#     "s5": {"address": "10101", "value": ""},
#     "s6": {"address": "10110", "value": ""},
#     "s7": {"address": "10111", "value": ""},
#     "s8": {"address": "11000", "value": ""},
#     "s9": {"address": "11001", "value": ""},
#     "s10": {"address": "11010", "value": ""},
#     "s11": {"address": "11011", "value": ""},
#     "t3": {"address": "11100", "value": ""},
#     "t4": {"address": "11101", "value": ""},
#     "t5": {"address": "11110", "value": ""},
#     "t6": {"address": "11111", "value": ""},
# }

with open("input.txt", 'r') as file:
    data = file.readlines()

with open("output.txt", 'w') as file:
    file.writelines("")

for j in range(len(data)):
    if data[j].strip()=='\n':
        pass
    else:
        data[j]=data[j].strip()

PC=-4 #Program Counter
bin = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(21)] ) )
def r_type(x):
    func=x[17:len(x)-12]
    if func=="000":
        pass
# print(data)
for x in data:
    if x[25:len(x)]=="0110011":
        r_type(x)