// test 1: large numbers
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load AddSub.asm,
output-file AddSub01.out,
compare-to AddSub01.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[3]%D2.6.2;

set PC 0,
set RAM[0] 0,  // Set R0
set RAM[1] 30000,  // Set R1
set RAM[2] 1,  // Set R2
set RAM[3] 30000;  // Set R3
repeat 100 {
  ticktock;    // Run for 100 clock cycles
}
set RAM[1] 30000, 
set RAM[2] 1,  
set RAM[3] 30000;
output;        // Output to file

