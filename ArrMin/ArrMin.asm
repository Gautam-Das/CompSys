// ArrMin.asm
// This program finds the smallest value in a given array and stores it in R0

// Initialize pointers
@R1
D=M        // D = address of the first element of the array (R1)
@addr      // Store the base address of the array in addr
M=D

@R2
D=M        // D = length of the array (R2)
@length
M=D        // Store the length in memory

// Set the initial minimum value to the first element of the array
@addr
A=M        // A = address of the first element
D=M        // D = *addr (value of the first element)
@R0
M=D        // Set R0 = initial minimum

// Start the loop
@i
M=1        // i = 1 (since we already took the first element)

(LOOP)
    @i
    D=M    // D = i (current index)
    @length
    D=D-M  // D = i - length
    @END
    D;JGE  // If i >= length, go to END

    // Compare current element with the minimum
    @addr
    D=M    // D = base address of array
    @i
    D=D+M  // D = addr + i (current element address)
    A=D    // A = RAM[addr + i]
    D=M    // D = RAM[addr + i] (current element)
    @R0
    D=D-M  // D = current element - R0 (current min)
    @SKIP
    D;JGE  // If current element >= min, skip to SKIP

    // Update min if the current element is smaller
    @addr
    D=M    // D = base address
    @i
    D=D+M  // D = addr + i
    A=D    // A = RAM[addr + i]
    D=M    // D = current element
    @R0
    M=D    // R0 = current element (new min)

(SKIP)
    // Increment i and repeat
    @i
    M=M+1
    @LOOP
    0;JMP  // Go back to LOOP

(END)
    @END
    0;JMP  // Infinite loop at the end
