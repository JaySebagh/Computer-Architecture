"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0b00000000] * 256
        self.register = [0] * 8
        self.pc = 0
        self.sp = 7
        self.register[self.sp] = 0xf4  
        self.instruction = {
            "0010": self.ldi,
            "0111": self.prn,
            "0001": self.hlt,
            "0101": self.push,
            "0110": self.pop
        }
        self.instruction_alu = {
            "0010": self.mul
        }

    def ram_read(self, address):
        return self.ram[address]
    
    def ram_write(self, value, address):
        self.ram[address] = value

    def ldi(self, opA, opB):
        self.register[opA] = opB
        self.pc += 1

    def prn(self, opA):
        print(self.register[opA])
        self.pc += 1

    def hlt(self):
        exit()
    
    def mul(self, opA, opB):
        print(self.alu("MUL", opA, opB))
        self.pc += 1
    
    def push(self, number):
        self.register[self.sp] -= 1  # decrement sp
        reg_val = self.register[number] # get value from register number
        self.ram[self.register[self.sp]] = reg_val  # copy reg value into memory at address SP
        self.pc += 1
    
    def pop(self, register):
        val = self.ram[self.register[self.sp]] # copy value from the memory
        self.register[register] = val  # copy val from memory at SP into register
        self.register[self.sp] += 1  # increment SP
        self.pc += 1

    def load(self, program):
        """Load a program into ram."""

        address = 0

        with open(program) as f:
            for line in f:
                line = line.split("#")[0]
                line = line.strip()
                if line == '':
                    continue
                self.ram[address] = int(line, 2)
                address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.register[reg_a] = self.register[reg_a] * self.register[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    # def trace(self):
    #     """
    #     Handy function to print out the CPU state. You might want to call this
    #     from run() if you need help debugging.
    #     """

    #     print(f"TRACE: %02X | %02X %02X %02X |" % (
    #         self.pc,
    #         #self.fl,
    #         #self.ie,
    #         self.ram_read(self.pc),
    #         self.ram_read(self.pc + 1),
    #         self.ram_read(self.pc + 2)
    #     ), end='')

    #     for i in range(8):
    #         print(" %02X" % self.reg[i], end='')

    #     print()

    def run(self):
        while True:
            ir = self.ram[self.pc]
            byte = bin(ir)[2:].zfill(8)
            deconstruct = "0b" + byte
            aa = deconstruct[2:4]
            b = deconstruct[4:5]
            c = deconstruct[5:6]
            dddd = deconstruct[6:]
            opA = None
            opB = None

            if aa == "01":
                self.pc += 1
                opA = self.ram[self.pc]
            elif aa== "10":
                self.pc += 1
                opA = self.ram[self.pc]
                self.pc += 1
                opB = self.ram[self.pc]
            if b == "0":
                if opA is not None and opB is not None:
                    self.instruction[dddd](opA, opB)
                elif opA is None and opB is not None:
                    self.instruction[dddd](opB)
                elif opA is not None and opB is None:
                    self.instruction[dddd](opA)
                else:
                    self.instruction[dddd]()
            else:
                if opA is not None and opB is not None:
                    self.instruction_alu[dddd](opA, opB)
                elif opA is None and opB is not None:
                    self.instruction_alu[dddd](opB)
                elif opA is not None and opB is None:
                    self.instruction_alu[dddd](opA)
                else:
                    self.instruction_alu[dddd]()

