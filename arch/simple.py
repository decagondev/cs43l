import sys
HALT = 1
PRINT_BOB = 2
PRINT_NUM = 3
STORE = 4
PRINT_REG = 5
PUSH = 6
POP = 7
CALL = 8
RET = 9
ADD = 10
LDI = 0b10000010
HLT = 0b00000001


def alu(op, opa, opb):
    if op == "ADD":
        reg[opa] += reg[opb]

ram = [0] * 256

sp = 7

reg = [0] * 8
reg[sp] = 0xf4

# our program
ram[0] = PRINT_BOB
ram[1] = PRINT_BOB
ram[2] = PRINT_NUM
ram[3] = 34
ram[4] = STORE
ram[5] = 0
ram[6] = 120
ram[7] = PRINT_REG
ram[8] = 0
ram[9] = PUSH
ram[10] = 0
ram[11] = STORE
ram[12] = 0
ram[13] = 12
ram[14] = PRINT_REG
ram[15] = 0
ram[16] = POP
ram[17] = 0
ram[18] = PRINT_REG
ram[19] = 0
ram[20] = STORE
ram[21] = 1
ram[22] = 2
ram[23] = STORE
ram[24] = 3
ram[25] = 31
ram[26] = CALL
ram[27] = 3
ram[28] = PRINT_REG
ram[29] = 3
ram[30] = HALT
ram[31] = ADD
ram[32] = 3
ram[33] = 0
ram[34] = RET


def load(filename):
    with open(filename) as filedata:
        addr = 0
        for line in filedata:
            
            data = line.split('#')[0].strip()
            if data == "":
                continue

            num = int(data)
            ram[addr] = num
            # self.ram_write(addr, num)
            addr += 1
        
# if len(sys.argv) != 2:
#     print(f"Usage: simple.py <filename>")
#     sys.exit(1)
    
# load(sys.argv[1])

pc = 0

running = True

while running:
    inst = ram[pc]
    opera = ram[pc + 1]
    operb = ram[pc + 2]
    

    if inst == HALT:
        print("Halting CPU")
        running = False
    elif inst == PRINT_BOB:
        print("BOB")
        pc += 1
    elif inst == PRINT_NUM:
        print(ram[pc + 1])
        pc += 2
    elif inst == STORE:
        reg_index = ram[pc + 1]
        data = ram[pc + 2]
        reg[reg_index] = data
        pc += 3
    elif inst == PRINT_REG:
        reg_index = ram[pc + 1]
        print(reg[reg_index])
        pc += 2
    elif inst == PUSH:
        # dec the SP
        reg[sp] -= 1
        # grab the index to the reg
        reg_index = ram[pc + 1]

        #get the value from the reg
        value = reg[reg_index]
        ram[reg[sp]] = value
        pc += 2

    elif inst == POP:
        # grab the index to the reg
        reg_index = ram[pc + 1]
        # get the value from the top of the stack
        value = ram[reg[sp]]
        # inc my stack pointer
        reg[sp] += 1
        reg[reg_index] = value

        pc += 2

    elif inst == ADD:
        alu("ADD", opera, operb)
        pc += 3

    elif inst == CALL:
        # store the return addr
        return_addr = pc + 2

        # dec the SP
        reg[sp] -= 1
        ram[reg[sp]] = return_addr


        # set pc to addr that is called
        reg_index = ram[pc + 1]
        pc = reg[reg_index]

    elif inst == RET:
        pc = ram[reg[sp]]
        reg[sp] += 1
