@R0
M=0

@R1
D=M
@END
D;JEQ

@R2
D=M
@END
D;JEQ
@NEG
D;JLT
@POS
D;JGT

(NEG)
    (WHILE1)
        @R2
        D=M
        @END1
        D;JGE
        @R2
        M=M+1
        @R1
        D=M
        @R0
        M=D+M
        @WHILE1
        0;JMP

    (END1)
        @R0
        M=-M
        @END
        0;JMP

(POS)
    (WHILE2)
        @R2
        D=M
        @END
        D;JLE
        @R2
        M=M-1
        @R1
        D=M
        @R0
        M=D+M
        @WHILE2
        0;JMP
    

(END)
    @END
    0;JMP