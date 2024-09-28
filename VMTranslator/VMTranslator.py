def segmentReformatter(seg, idx):
    if (seg == "this"):
        return "THIS"

    if (seg == "that"):
        return "THAT"

    if (seg == "argument"):
        return "ARG"
    
    if (seg == "local"):
        return "LCL"
    
    if (seg == "static"):
        return str(16 + idx)

    if (seg == "pointer"):
        return "R" + str(3 + idx)

    if (seg == "temp"):
        return "R" + str(5 + idx)

    if (seg == "constant"):
        return str(idx)
    
    return seg

class VMTranslator:
    labelCount = 0
    
    def newUniqueLabel():
        uniqueLabel = str(VMTranslator.labelCount)
        VMTranslator.labelCount += 1
        return uniqueLabel

    def vm_push(seg, idx):
        '''Generate Hack Assembly code for a VM push operation'''
        resolvedSeg = segmentReformatter(seg, idx)
        resultCode = ""
        if (seg == "constant" or seg == "static" or seg == "pointer" or seg == "temp"):
            resultCode += "@" + resolvedSeg + "\n"
            if seg == "constant":
                resultCode += "D = A\n"
            else:
                resultCode += "D = M\n"
        elif (seg == "local" or seg == "this" or seg == "that" or seg == "argument"):
            resultCode += "@" + resolvedSeg + "\n"
            resultCode += "D = M\n"
            resultCode += "@" + str(idx) + "\n"
            resultCode += "A = D + A\n"
            resultCode += "D=M\n"
        
        resultCode += "@SP\n"
        resultCode += "A=M\n"
        resultCode += "M=D\n"
        resultCode += "@SP\n"
        resultCode += "M = M+1"

        return resultCode

    def vm_pop(seg, idx):
        '''Generate Hack Assembly code for a VM pop operation'''
        resolvedSeg = segmentReformatter(seg, idx)
        resultCode = "@" + resolvedSeg + "\n"
        
        if (seg == "static" or seg == "temp" or seg == "pointer"):
            resultCode += "D = A\n"
        elif (seg == "local" or seg == "this" or seg == "that" or seg == "argument"):
            resultCode += "D = M\n"
            resultCode += "@" + str(idx) + "\n"
            resultCode += "D = D + A\n"

        resultCode += "@R13\n"
        resultCode += "M = D\n"
        resultCode += "@SP\n"
        resultCode += "AM = M -1\n"
        resultCode += "D=M\n"
        resultCode += "@R13\n"
        resultCode += "A=M\n"
        resultCode += "M=D"

        return resultCode

    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "A = A-1\n"
        resultCode += "M = D + M"

        return resultCode

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "A = A-1\n"
        resultCode += "M = M - D"

        return resultCode

    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        resultCode = "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = !M\n"
        resultCode += "M = M + 1"

        return resultCode

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        uniqueLabel = VMTranslator.newUniqueLabel()

        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "A = A-1\n"
        resultCode += "D = M - D\n"
        resultCode += "@EQ.true_" + uniqueLabel + "\n"
        resultCode += "D;JEQ\n"
        resultCode += "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = 0\n"
        resultCode += "@EQ.skip_" + uniqueLabel + "\n"
        resultCode += "0;JMP\n"
        resultCode += "(EQ.true_" + uniqueLabel + ")\n"
        resultCode += "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = -1\n"
        resultCode += "(EQ.skip_" + uniqueLabel + ")"
        return resultCode

    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        uniqueLabel = VMTranslator.newUniqueLabel()
        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "A = A-1\n"
        resultCode += "D = M - D\n"
        resultCode += "@GT.true" + uniqueLabel + "\n"
        resultCode += "D;JGT\n"
        resultCode += "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = 0\n"
        resultCode += "@GT.skip" + uniqueLabel + "\n"
        resultCode += "0;JMP\n"
        resultCode += "(GT.true" + uniqueLabel + ")\n"
        resultCode += "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = -1\n"
        resultCode += "(GT.skip" + uniqueLabel + ")"
        return resultCode

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        uniqueLabel = VMTranslator.newUniqueLabel()
        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "A = A-1\n"
        resultCode += "D = M - D\n"
        resultCode += "@LT.true" + uniqueLabel + "\n"
        resultCode += "D;JLT\n"
        resultCode += "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = 0\n"
        resultCode += "@LT.skip" + uniqueLabel + "\n"
        resultCode += "0;JMP\n"
        resultCode += "(LT.true" + uniqueLabel + ")\n"
        resultCode += "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = -1\n"
        resultCode += "(LT.skip" + uniqueLabel + ")"
        return resultCode

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "A = A-1\n"
        resultCode += "M = M&D"
        return resultCode

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "A = A-1\n"
        resultCode += "M = M|D"
        return resultCode

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        resultCode = "@SP\n"
        resultCode += "A = M-1\n"
        resultCode += "M = !M"
        return resultCode

    def vm_label(lbl):
        '''Generate Hack Assembly code for a VM label operation'''
        resultCode = "(" + lbl + ")"
        return resultCode

    def vm_goto(lbl):
        '''Generate Hack Assembly code for a VM goto operation'''
        resultCode = "@" + lbl + "\n"
        resultCode += "0;JMP"
        return resultCode

    def vm_if(lbl):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        resultCode = "@SP\n"
        resultCode += "AM = M-1\n"
        resultCode += "D = M\n"
        resultCode += "@" + lbl + "\n"
        resultCode += "D;JNE"

        return resultCode

    def vm_function(funcName, numVars):
        '''Generate Hack Assembly code for a VM function operation'''
        resultCode = "(FUNC.defMod." + funcName + ")\n"
        resultCode += "@SP\n"
        resultCode += "A = M\n"
        for i in range(numVars):
            resultCode += "M=0\n"
            resultCode += "A=A+1\n"
        resultCode += "D=A\n"
        resultCode += "@SP\n"
        resultCode += "M=D"

        return resultCode

    def vm_call(funcName, numArgs):
        '''Generate Hack Assembly code for a VM call operation'''
        uniqueLabel = VMTranslator.newUniqueLabel()

        resultCode = "@SP\n"
        resultCode += "D=M\n"
        resultCode += "@R13\n"
        resultCode += "M=D\n"
        
        resultCode += "@RET." + uniqueLabel + "\n"
        resultCode += "D=A\n"
        resultCode += "@SP\n"
        resultCode += "A=M\n"
        resultCode += "M=D\n"

        resultCode += "@SP\n"
        resultCode += "M=M+1\n"

        resultCode += "@LCL\n"
        resultCode += "D=M\n"
        resultCode += "@SP\n"
        resultCode += "A=M\n"
        resultCode += "M=D\n"

        resultCode += "@SP\n"
        resultCode += "M=M+1\n"

        resultCode += "@ARG\n"
        resultCode += "D=M\n"
        resultCode += "@SP\n"
        resultCode += "A=M\n"
        resultCode += "M=D\n"
        
        resultCode += "@SP\n"
        resultCode += "M=M+1\n"

        resultCode += "@THIS\n"
        resultCode += "D=M\n"
        resultCode += "@SP\n"
        resultCode += "A=M\n"
        resultCode += "M=D\n"

        resultCode += "@SP\n"
        resultCode += "M=M+1\n"

        resultCode += "@THAT\n"
        resultCode += "D=M\n"
        resultCode += "@SP\n"
        resultCode += "A=M\n"
        resultCode += "M=D\n"

        resultCode += "@SP\n"
        resultCode += "M=M+1\n"

        resultCode += "@R13\n"
        resultCode += "D=M\n"
        resultCode += "@" + str(numArgs) + "\n"
        resultCode += "D=D-A\n"
        resultCode += "@ARG\n"
        resultCode += "M=D\n"

        resultCode += "@SP\n"
        resultCode += "D=M\n"
        resultCode += "@LCL\n"
        resultCode += "M=D\n"
        resultCode += "@FUNC.defMod." + funcName + "\n"
        resultCode += "0;JMP\n"
        resultCode += "(RET." + uniqueLabel + ")"

        return resultCode

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        resultCode = "@LCL\n"
        resultCode += "D=M\n"
        resultCode += "@5\n"
        resultCode += "A=D-A\n"
        resultCode += "D=M\n"
        resultCode += "@R13\n"
        resultCode += "M=D\n"

        resultCode += "@SP\n"
        resultCode += "A=M-1\n"
        resultCode += "D=M\n"
        resultCode += "@ARG\n"
        resultCode += "A=M\n"
        resultCode += "M=D\n"

        resultCode += "D=A+1\n"
        resultCode += "@SP\n"
        resultCode += "M=D\n"

        resultCode += "@LCL\n"
        resultCode += "AM=M-1\n"
        resultCode += "D=M\n"
        resultCode += "@THAT\n"
        resultCode += "M=D\n"

        resultCode += "@LCL\n"
        resultCode += "AM=M-1\n"
        resultCode += "D=M\n"
        resultCode += "@THIS\n"
        resultCode += "M=D\n"

        resultCode += "@LCL\n"
        resultCode += "AM=M-1\n"
        resultCode += "D=M\n"
        resultCode += "@ARG\n"
        resultCode += "M=D\n"

        resultCode += "@LCL\n"
        resultCode += "A=M-1\n"
        resultCode += "D=M\n"
        resultCode += "@LCL\n"
        resultCode += "M=D\n"

        resultCode += "@R13\n"
        resultCode += "A=M\n"
        resultCode += "0;JMP"

        return resultCode

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        