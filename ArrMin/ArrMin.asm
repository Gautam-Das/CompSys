@R1
D=M
@R2
D=M+D
@16383
D=A-D
@END
D;JLT // end early if array exceeds address 16383


@R1
D=M

@END
D=D-1
D=D-1
D;JLE // end early if array starts at or before address 2


// set min
@R1
A=M
D=M
@R0
M=D 

@R2
D=M
@END
D;JLE // end if length < 0



(Loop)
@R2
D = M

@R1
D=D-1
A = M + D
D = M

@BPOS
D;JGE

@R0
D = M
@BNEGAPOS
D;JGE

@NNPP
A;JMP

(BPOS)
@R0
D = M
@keepTemp
D;JLE
//CONTINUE WITH both neg both positive program
@NNPP
A;JMP


(BNEGAPOS)
@R2
D = M

@R1
D=D-1
A = M + D
D = M

@R0
M=D
@keepTemp
A;JMP

(NNPP)
@R2
D = M

@R1
D=D-1
A = M + D
D = M

@R0
D = M-D

@keepTemp
D;JLE

@R2
D=M

@R1
D=D-1
A = M + D
D = M

@R0
M=D

@R4
M = D

(keepTemp)
@R2
M = M-1
D = M

@Loop
D;JGT

(END)
@END
A;JMP