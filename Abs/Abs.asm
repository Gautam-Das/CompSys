@R1
D=M
@POS
D;JGE
@NEG
D;JLT

(POS)
    @R0
    M=D
    @END
    0;JMP

(NEG)
    @R0
    M=-D
    @END
    0;JMP

(END)
    @END
    0;JMP