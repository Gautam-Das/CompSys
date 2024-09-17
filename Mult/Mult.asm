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

@POS
D;JGT

D=!D
D=D+1

(POS)
@R3
M=D

(WHILE)
    @R1
    D=M
    @R0
    M=M+D

    @R3
    M=M-1
    D=M
    @WHILE
    D;JGT

@R2
D=M
@NEG
D;JLT


(END)
    @END
    0;JMP

(NEG)
    @R0
    M=!M
    M=M+1
    @END
    0;JMP