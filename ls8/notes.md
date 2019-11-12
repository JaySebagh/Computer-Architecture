HLT = hault/stop
LDI = load "immediate", store a value in a register, or "set this register to this value".
PRN: a pseudo-instruction that prints the numeric value stored in a register.

LDI --> store value in register
PRN --> return value in register

MAR: Memory Address Register, holds the memory address we're reading or writing
MDR: Memory Data Register, holds the value to write or the value just read

MAR --> address
MDR --> data that we are going to either use to update, or the data that we read

PC: Program Counter, address of the currently executing instruction
IR: Instruction Register, contains a copy of the currently executing instruction

PC --> counter/address
IR --> holds current instructions




Meanings of the bits in the first byte of each instruction: AABCDDDD

AA Number of operands for this opcode, 0-2
B 1 if this is an ALU operation
C 1 if this instruction sets the PC
DDDD Instruction identifier


211addition


10000010

