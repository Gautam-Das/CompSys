@R1
D=M
@R3
M=D

@R2
D=M
@R4
M=D

@R5
M=0

(GETMIN)
    @R1
    A=M //get address if current element
    D=M //store value of current element
    @R0
    M=D //store  first value in minimum

    (WHILE)
        // check if R2 = 0
        @R2
        D=M
        @CHANGEARRAY
        D;JEQ
        
        // Decrement  R2
        @R2
        M=M-1

        // Get curretn element
        @R1 
        A=M
        D=M

        // find difference between current minimum and new minimum
        @R0
        D=M-D
        
        // jump if M-D>0 i.e. M>D
        @minimum
        D;JGT
        
        @continue
        0;JMP


        (minimum)
            // Track address of minimum element
            @R1
            D=M
            @R5
            M=D

            // Get current element
            @R1 
            A=M
            D=M
            //  change  minimum
            @R0
            M=D
            @continue 
            0;JMP

        (continue)
            // increase memory address
            @R1
            M=M+1
            @WHILE  
            0;JMP

    
(CHANGEARRAY)
@R3
A=M
D=M
@R5
A=M
M=D

@R0
D=M
@R3
A=M
M=D
@R3
M=M+1

@R4
DM=M-1
@END
D;JEQ

@R3
D=M
@R1
M=D

@R4
D=M
@R2
M=D

@R0
M=-1

@GETMIN
0;JMP



(END)
    @END
    0;JMP
