// test 3 : array overlap
// Follows the Test Scripting Language format described in 
// Appendix B of the book "The Elements of Computing Systems"

load ArrSort.asm,
output-file ArrSort03.out,
compare-to ArrSort03.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0]  0,  // Set R0
set RAM[1]  0, // Set R1
set RAM[2]  4,  // Set R2

repeat 600 {
  ticktock;    // Run for 600 clock cycles
}
set RAM[1] 0,  // Restore arguments in case program used them
set RAM[2] 4,
output;        // Output to file

