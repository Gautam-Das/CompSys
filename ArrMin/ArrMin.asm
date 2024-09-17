@R2
D=M
@END
D;JLE

@R1
A=M //get address if current element
D=M //store value of current element

@R0
M=D //store  first value in minimum

(WHILE)
    // check if R2 = 0
    @R2
    D=M
    @END
    D;JEQ
    
    // Decrement  R2
    @R2
    M=M-1

    @R0
    D=M
    @Mpos
    D;JGT
    @Mneg
    D;JMP

    (FindDifference)
        // Get current element
        @R1 
        A=M
        D=M

        // find difference between current minimum and current element
        @R0
        D=M-D
        
        // jump if M-D>0 i.e. M>D
        @minimum
        D;JGT
        
        @continue
        0;JMP


    (minimum)
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

(END)
    @END
    0;JMP


(Mpos)
    // if d is neg and m is positive, d<m hence, go to minimum, otherwise FindDifference
    @R1 
    A=M
    D=M

    @minimum
    D;JLT
    @FindDifference
    D;JMP


(Mneg)
    // if d is pos and m is negative, d>m, hence continue, otherwise got to finddifference
    @R1 
    A=M
    D=M

    @continue
    D;JGT
    @FindDifference
    D;JMP