// i, j, temp;
@R2
D=M-1
@I
M=D
@TEMP
M=0

//    for (i = (array_size - 1); i>= 0; i--)
(ILOOP)
    @I
    D=M
    @END
    D;JLT
    @J
    M=1

    (JLOOP)
        @J
        D=M
        @I
        D=M-D // I-J
        @ILOOPCONT
        D;JLT

        @J
        D=M
        @R1
        A=D+M
        D=M
        @JPOS
        D;JGT
        @JNEG
        D;JMP
        

        //if (numbers[j-1] > numbers[j])
        (SWAP)
            @J
            D=M-1
            @R1
            A=D+M
            D=M // D= J-1
            @TEMP
            M=D

            @J
            D=M
            @R1
            A=D+M
            D=M // D= J
            A=A-1 // A POINTS TO J-1
            M=D

            A=A+1 // A POINTS TO J
            D=A // D POINTS TO J
            
            @JADDRESS
            M=D

            @TEMP
            D=M

            @JADDRESS
            A=M
            M=D


        (CONTINUE)
            @J
            M=M+1
            @JLOOP
            0;JMP
    
    (ILOOPCONT)
        @I
        M=M-1
        @ILOOP
        0;JMP
    
(END)
    @R0
    M=-1
    @END
    0;JMP

(JPOS)
    // if j-1 < 0, then j-1<j else check diff
    @J
    D=M-1
    @R1
    A=D+M
    D=M
    @CONTINUE
    D;JLT
    @DIFF
    D;JMP

(JNEG)
    // if j-1 >0 , then j-1>j else check diff
    @J
    D=M-1
    @R1
    A=D+M
    D=M
    @SWAP
    D;JGT
    @DIFF
    D;JMP

(DIFF)
    @J
    D=M-1
    @R1
    A=D+M
    D=M // D= J-1
    A=A+1 // A POINTS TO J
    D=D-A // (J-1)-J
    @SWAP
    D;JGT
    @CONTINUE
    D;JMP