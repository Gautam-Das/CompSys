@R0
M=0

(WHILE)
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
    @WHILE
    0;JMP

(END)
    @END
    0;JMP
